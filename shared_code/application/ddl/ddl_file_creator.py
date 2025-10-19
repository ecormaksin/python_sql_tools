import json
import pprint
from pathlib import Path
from typing import Optional

from shared_code.application.app_directory_creator import AppDirectoryCreator
from shared_code.application.app_file_utils import AppFileUtils
from shared_code.domain.ddl.create_target.list import DDLCreateTargetList
from shared_code.domain.table_dependency.map import TableDependencyMap
from shared_code.infra.database.mysql.connector import MySQLConnector
from shared_code.infra.database.mysql.table_dependency_map_base_getter import (
    TableDependencyMapBaseGetter,
)


class DDLFileCreator:
    @classmethod
    def execute(
        cls,
        db_config_json_file_path_str: Optional[str],
        ddl_directory_path_str: Optional[str],
        ddl_file_name: Optional[str],
    ) -> str:
        db_config_file_path_str = AppFileUtils.determine_and_check(
            arg_file_path_str=db_config_json_file_path_str,
            default_file_path=Path(__file__).parent.parent.parent.parent.joinpath(
                "db_config.json"
            ),
        )

        ddl_dir_path_str = AppDirectoryCreator.execute(
            module_name="dml_source_xlsx",
            directory_type="xlsx output",
            directory_path_str=ddl_directory_path_str,
        )

        a_ddl_file_name = ddl_file_name if ddl_file_name else "ddl.sql"

        ddl_file_path = Path(ddl_dir_path_str).joinpath(a_ddl_file_name)
        ddl_file_path_str = str(ddl_file_path)

        with open(db_config_file_path_str, "r", encoding="utf-8") as file_obj:
            dict_obj = json.load(file_obj)
            ddl_targets = dict_obj.get("ddl_target", [{"schema": dict_obj["database"]}])
            ddl_create_target_list = DDLCreateTargetList.from_dict_list(
                dict_list=ddl_targets
            )

        table_dependency_map = TableDependencyMap.empty()
        for ddl_create_target in ddl_create_target_list.unmodifiable_elements:
            schema = ddl_create_target.schema
            schema_value = schema.value

            with MySQLConnector(
                config_json_file_path_str=db_config_file_path_str
            ).override_database(database=schema_value) as db_connector:
                db_connection = db_connector.connect()
                with db_connection.cursor(buffered=True, dictionary=True) as cursor:
                    table_dependency_map = TableDependencyMapBaseGetter.execute(
                        cursor=cursor,
                        table_dependency_map=table_dependency_map,
                        schema=schema,
                    )
                    pprint.pprint(table_dependency_map)


        return ddl_file_path_str