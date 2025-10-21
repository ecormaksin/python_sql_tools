import json
from pathlib import Path
from typing import Optional

from shared_code.application.app_directory_creator import AppDirectoryCreator
from shared_code.application.app_file_utils import AppFileUtils
from shared_code.domain.ddl.create_target.map import DDLCreateTargetMap
from shared_code.domain.table.table_type import TableType
from shared_code.domain.table_dependency.map import TableDependencyMap
from shared_code.infra.database.mysql.connector import MySQLConnector
from shared_code.infra.database.mysql.create_table_statement_getter import (
    CreateTableStatementGetter,
)
from shared_code.infra.database.mysql.create_view_statement_getter import (
    CreateViewStatementGetter,
)
from shared_code.infra.database.mysql.table_dependency_map_base_getter import (
    TableDependencyMapBaseGetter,
)
from shared_code.infra.database.mysql.table_dependency_table_reference_getter import (
    TableDependencyTableReferenceGetter,
)
from shared_code.infra.database.mysql.table_dependency_view_reference_getter import (
    TableDependencyViewReferenceGetter,
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
            module_name="ddl",
            directory_type="ddl output",
            directory_path_str=ddl_directory_path_str,
        )

        a_ddl_file_name = ddl_file_name if ddl_file_name else "ddl.sql"

        ddl_file_path = Path(ddl_dir_path_str).joinpath(a_ddl_file_name)
        ddl_file_path_str = str(ddl_file_path)

        with open(db_config_file_path_str, "r", encoding="utf-8") as file_obj:
            dict_obj = json.load(file_obj)
            ddl_targets = dict_obj.get("ddl_target", [{"schema": dict_obj["database"]}])
            ddl_create_target_map = DDLCreateTargetMap.from_dict_list(
                dict_list=ddl_targets
            )

        table_dependency_map = TableDependencyMap.empty()
        for ddl_create_target in ddl_create_target_map.unmodifiable_elements.values():
            schema = ddl_create_target.schema

            with MySQLConnector(
                config_json_file_path_str=db_config_file_path_str
            ).override_database(schema=schema) as db_connector:
                db_connection = db_connector.connect()
                with db_connection.cursor(buffered=True, dictionary=True) as cursor:
                    table_dependency_map = TableDependencyMapBaseGetter.execute(
                        cursor=cursor,
                        table_dependency_map=table_dependency_map,
                        schema=schema,
                    )

                    table_dependency_map = TableDependencyTableReferenceGetter.execute(
                        cursor=cursor,
                        table_dependency_map=table_dependency_map,
                        schema=schema,
                    )

                    table_dependency_map = TableDependencyViewReferenceGetter.execute(
                        cursor=cursor,
                        table_dependency_map=table_dependency_map,
                        schema=schema,
                    )

        for (
            table_name_with_schema,
            table_dependency,
        ) in table_dependency_map.unmodifiable_elements.items():
            dependent_table_set = table_dependency.dependent_table_set

            for dependent_table in dependent_table_set.unmodified_elements():
                another_table_dependency = table_dependency_map.get(key=dependent_table)
                dependent_table_set = dependent_table_set.union(
                    other=another_table_dependency.dependent_table_set
                )

            new_table_dependency = table_dependency.update_dependent_table_set(
                dependent_table_set=dependent_table_set
            )

            table_dependency_map = table_dependency_map.put(
                key=table_name_with_schema,
                value=new_table_dependency,
            )

        table_dependency_list = sorted(
            list(table_dependency_map.unmodifiable_elements.values())
        )

        ddl_lines: list[str] = list()
        for table_dependency in table_dependency_list:
            table_name_with_schema = table_dependency.table_name_with_schema
            schema = table_name_with_schema.schema
            table_name = table_name_with_schema.table_name
            table_name_value = table_name.value

            ddl_create_target = ddl_create_target_map.get(key=schema)

            if ddl_create_target.is_not_target(table_name=table_name):
                continue

            with MySQLConnector(
                config_json_file_path_str=db_config_file_path_str
            ).override_database(schema=schema) as db_connector:
                db_connection = db_connector.connect()
                with db_connection.cursor(buffered=True, dictionary=True) as cursor:
                    if table_dependency.table_type == TableType.BASE_TABLE:
                        ddl_lines.append(
                            f"DROP TABLE IF EXISTS `{table_name_value}` CASCADE;"
                        )
                        ddl_lines.append("")

                        create_table_statement = CreateTableStatementGetter.execute(
                            cursor=cursor, table_name=table_name
                        )
                        ddl_lines.extend(create_table_statement)
                        ddl_lines.append("")

                    if table_dependency.table_type == TableType.VIEW:
                        ddl_lines.append(
                            f"DROP VIEW IF EXISTS `{table_name_value}` CASCADE;"
                        )
                        ddl_lines.append("")

                        create_view_statement = CreateViewStatementGetter.execute(
                            cursor=cursor, view_name=table_name
                        )
                        ddl_lines.append(create_view_statement)
                        ddl_lines.append("")

        with open(ddl_file_path_str, "w", encoding="utf-8") as file_obj:
            file_obj.write("\n".join(ddl_lines))

        return ddl_file_path_str