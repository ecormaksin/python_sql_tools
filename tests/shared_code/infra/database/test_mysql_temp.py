import dataclasses
import re
from typing import Optional

from sqlalchemy import create_engine, text
from sqlalchemy_utils import create_database, database_exists
from testcontainers.mysql import MySqlContainer

from tests.project_root_resolver import ProjectRootResolver
from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator_map import (
    EntityCreatorMap,
)

from pathlib import Path
from mysql.connector import connect

from dataclasses import dataclass

@dataclass
class DDLFileNameControlEntity:
    NUMBER_LENGTH = 2

    schema_name: str
    view: Optional[int] = None

    def get_file_name(self, serial_number: int) -> str:
        return str(serial_number).zfill(self.NUMBER_LENGTH) + "." + self.schema_name + ".sql"

    def get_view_file_name(self) -> str:
        if not self.view:
            raise RuntimeError("ビューのファイル名連番を指定してください。")

        return self.get_file_name(self.view)

@dataclass
class DDLFileNameControlEntityList:
    a_list = [
        DDLFileNameControlEntity(schema_name="artist"),
        DDLFileNameControlEntity(schema_name="genre"),
        DDLFileNameControlEntity(schema_name="media_type"),
        DDLFileNameControlEntity(schema_name="album", view=1),
        DDLFileNameControlEntity(schema_name="play_list"),
        DDLFileNameControlEntity(schema_name="employee"),
        DDLFileNameControlEntity(schema_name="customer"),
        DDLFileNameControlEntity(schema_name="invoice")
    ]

    @classmethod
    def get(cls) -> list[DDLFileNameControlEntity]:
        return DDLFileNameControlEntityList.a_list

class TestClass:
    USER_NAME = "root"
    ROOT_PASSWORD = "test"

    def test(self):
        project_root = ProjectRootResolver.execute(Path(__file__).resolve())

        common_relative_dirs = ["sample", "docker", "mysql", "setup"]

        schema_ddl_relative_dirs = list(common_relative_dirs)
        schema_ddl_relative_dirs.append("01.create_databases")
        schema_ddl_dir = project_root.joinpath(*schema_ddl_relative_dirs)

        table_ddl_relative_dirs = list(common_relative_dirs)
        table_ddl_relative_dirs.append("02.create_tables")
        table_ddl_dir = project_root.joinpath(*table_ddl_relative_dirs)

        view_ddl_relative_dirs = list(common_relative_dirs)
        view_ddl_relative_dirs.append("03.create_views")
        view_ddl_dir = project_root.joinpath(*view_ddl_relative_dirs)

        with MySqlContainer(
            image="mysql:9.5.0-oraclelinux9", username=TestClass.USER_NAME, root_password=TestClass.ROOT_PASSWORD
        ) as db_container:
            original_url = db_container.get_connection_url()

            test_db_config_dict = {
                "host": "localhost",
                "user": TestClass.USER_NAME,
                "password": TestClass.ROOT_PASSWORD,
                "port": db_container.get_exposed_port(3306),
                "database": db_container.dbname,
            }
            test_db_conn = connect(**test_db_config_dict)

            for index, ctrl_entity in enumerate(DDLFileNameControlEntityList.get(), start=1):
                schema_name = ctrl_entity.schema_name
                print(f"====={schema_name}")

                with test_db_conn.cursor(buffered=True, dictionary=True) as test_db_cursor:
                    query = """
                    select 
                      SCHEMA_NAME as schema_name
                    from 
                      INFORMATION_SCHEMA.SCHEMATA
                    where 
                      SCHEMA_NAME = %(schema_name)s
                    """
                    test_db_cursor.execute(query, {"schema_name": schema_name})
                    schema_names_result = test_db_cursor.fetchall()

                    ddl_file_name = ctrl_entity.get_file_name(serial_number=index)

                    if len(schema_names_result):
                        print(f"データベース「{schema_name}」は存在しています。")
                    else:
                        print(f"データベース「{schema_name}」は存在していません。")

                        schema_ddl_file = schema_ddl_dir.joinpath(ddl_file_name)
                        with open(schema_ddl_file) as f:
                            ddl = f.read()
                            test_db_cursor.execute(ddl)

                    db_config_dict = dict(test_db_config_dict)
                    db_config_dict["database"] = schema_name
                    db_conn = connect(**db_config_dict)

                    with db_conn.cursor(buffered=True, dictionary=True) as db_cursor:

                        table_ddl_file = table_ddl_dir.joinpath(ddl_file_name)
                        with open(table_ddl_file) as f:
                            file_content = f.read()
                            ddl_list = re.split(r"[; ]+(?:\r?\n)*", file_content)
                            for ddl in ddl_list:
                                db_cursor.execute(ddl)
