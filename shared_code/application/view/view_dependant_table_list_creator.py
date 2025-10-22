import json
from pathlib import Path
from typing import Optional

from shared_code.application.app_directory_creator import AppDirectoryCreator
from shared_code.application.app_file_utils import AppFileUtils
from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName
from shared_code.domain.table.table_type import TableType
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema
from shared_code.domain.table_name_with_schema.set import TableNameWithSchemaSet
from shared_code.infra.database.mysql.connector import MySQLConnector


class ViewDependantTableListCreator:
    @classmethod
    def execute(
        cls,
        view_name: str,
        db_config_json_file_path_str: Optional[str],
        list_directory_path_str: Optional[str],
        list_file_name: Optional[str],
    ) -> str:
        target_view_name = TableName(value=view_name)

        db_config_file_path_str = AppFileUtils.determine_and_check(
            arg_file_path_str=db_config_json_file_path_str,
            default_file_path=Path(__file__).parent.parent.parent.parent.joinpath(
                "db_config.json"
            ),
        )

        list_dir_path_str = AppDirectoryCreator.execute(
            module_name="view",
            directory_type="view dependant table list",
            directory_path_str=list_directory_path_str,
        )

        a_list_file_name = (
            list_file_name if list_file_name else "view_dependant_table_list.txt"
        )

        list_file_path = Path(list_dir_path_str).joinpath(a_list_file_name)
        list_file_path_str = str(list_file_path)

        with open(db_config_file_path_str, "r", encoding="utf-8") as file_obj:
            dict_obj = json.load(file_obj)
            target_schema = Schema(value=dict_obj["database"])

        dependant_table_set = TableNameWithSchemaSet.empty()

        first_search_view = TableNameWithSchema(
            schema=target_schema, table_name=target_view_name
        )
        search_view_set = TableNameWithSchemaSet(elements={first_search_view})

        while search_view_set.is_not_empty():
            for search_view in search_view_set.elements:
                a_schema = search_view.schema
                a_view_name = search_view.table_name

                with MySQLConnector(
                    config_json_file_path_str=db_config_file_path_str
                ).override_database(schema=a_schema) as db_connector:
                    db_connection = db_connector.connect()
                    with db_connection.cursor(buffered=True, dictionary=True) as cursor:
                        query = """
                            select 
                              vtu.TABLE_SCHEMA as table_schema,
                              vtu.TABLE_NAME as table_name,
                              t.TABLE_TYPE as table_type
                            from 
                              information_schema.VIEW_TABLE_USAGE vtu
                              inner join information_schema.TABLES t
                                on 
                                t.TABLE_SCHEMA = vtu.TABLE_SCHEMA 
                                and t.TABLE_NAME = vtu.TABLE_NAME 
                            where 
                              vtu.VIEW_SCHEMA = %s
                              and vtu.VIEW_NAME = %s
                          """

                        cursor.execute(query, (a_schema.value, a_view_name.value))
                        rows = cursor.fetchall()

                        for row in rows:
                            dependant_schema = Schema(value=row["table_schema"])
                            dependant_table_name = TableName(value=row["table_name"])

                            table_name_with_schema = TableNameWithSchema(
                                schema=dependant_schema, table_name=dependant_table_name
                            )
                            table_type = TableType.from_mysql_value(
                                mysql_value=row["table_type"]
                            )

                            if table_type == TableType.BASE_TABLE:
                                dependant_table_set = dependant_table_set.put(
                                    element=table_name_with_schema
                                )

                            if table_type == TableType.VIEW:
                                search_view_set = search_view_set.put(element=table_name_with_schema)


                search_view_set = search_view_set.remove(element=search_view)

        table_list: list[str] = []
        for dependant_table in dependant_table_set.unmodified_elements():
            table_list.append(str(dependant_table))

        with open(list_file_path_str, "w", encoding="utf-8") as file_obj:
            file_obj.write("\n".join(sorted(table_list)))

        return list_file_path_str