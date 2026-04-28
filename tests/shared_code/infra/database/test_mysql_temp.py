import re

from sqlalchemy import create_engine, text
from sqlalchemy_utils import create_database, database_exists
from testcontainers.mysql import MySqlContainer

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator_map import (
    EntityCreatorMap,
)

from mysql.connector import connect

class TestClass:
    USER_NAME = "root"
    ROOT_PASSWORD = "test"

    def test(self):
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

            entity_creator_map = EntityCreatorMap.get()

            for db_name, entity_creator in entity_creator_map.items():
                print(f"====={db_name}")

                with test_db_conn.cursor(buffered=True, dictionary=True) as test_db_cursor:
                    query = """
                    select 
                      SCHEMA_NAME as schema_name
                    from 
                      INFORMATION_SCHEMA.SCHEMATA
                    where 
                      SCHEMA_NAME = %(schema_name)s
                    """
                    test_db_cursor.execute(query, {"schema_name": db_name})
                    rows = test_db_cursor.fetchall()

                    if len(rows):
                        print(f"データベース「{db_name}」は存在しています。")
                    else:
                        print(f"データベース「{db_name}」は存在していません。")
