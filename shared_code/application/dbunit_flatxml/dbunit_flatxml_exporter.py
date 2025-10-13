import base64
from pathlib import Path
from typing import Optional

from shared_code.application.app_directory_creator import AppDirectoryCreator
from shared_code.application.app_file_utils import AppFileUtils
from shared_code.domain.table_name.set import TableNameSet
from shared_code.infra.database.mysql.connector import MySQLConnector
from shared_code.infra.database.mysql.entity_definitions_getter import (
    EntityDefinitionsGetRequest,
    EntityDefinitionsGetResponse,
    EntityDefinitionsGetter,
)


class DBUnitFlatXmlExporter:
    @classmethod
    def execute(cls,
                db_config_json_file_path_str: Optional[str],
                target_tables: Optional[str],
                xml_directory_path_str: Optional[str],
                ) -> str:

        db_config_file_path_str = AppFileUtils.determine_and_check(
            arg_file_path_str=db_config_json_file_path_str,
            default_file_path=Path(__file__).parent.parent.parent.parent.joinpath(
                "db_config.json"
            ),
        )

        xml_dir_path_str = AppDirectoryCreator.execute(
            module_name="dbunit_flatxml",
            directory_type="DBUnit FlatXML output",
            directory_path_str=xml_directory_path_str,
        )

        target_table_set = TableNameSet.from_csv_str(csv_str=target_tables)

        entity_definitions_get_request = EntityDefinitionsGetRequest(
            db_config_json_file_path_str=db_config_file_path_str,
            target_table_name_set=target_table_set,
        )
        entity_definitions_get_response = EntityDefinitionsGetter.execute(
            a_request=entity_definitions_get_request
        )

        cls.__export_xml(
            db_config_file_path_str=db_config_file_path_str,
            entity_definitions_get_response=entity_definitions_get_response,
            xml_dir_path_str=xml_dir_path_str
        )

        return xml_dir_path_str

    @classmethod
    def __export_xml(cls,
                     db_config_file_path_str: str,
                     entity_definitions_get_response: EntityDefinitionsGetResponse,
                     xml_dir_path_str: str):

        with MySQLConnector(
            config_json_file_path_str=db_config_file_path_str
        ) as db_connector:
            db_connection = db_connector.connect()
            with db_connection.cursor(buffered=True, dictionary=True) as cur:

                for entity_definition in entity_definitions_get_response.entity_definitions.unmodifiable_elements.values():
                    table_name = entity_definition.table_name
                    table_name_value = table_name.value

                    xml_lines: list[str] = ['<?xml version="1.0" encoding="UTF-8"?>', '<dataset>']

                    query = entity_definition.select_statement()

                    cur.execute(query)
                    rows = cur.fetchall()

                    for row in rows:
                        xml_line = "<" + table_name_value

                        for db_column in entity_definition.db_columns.unmodifiable_elements:
                            column_value = row[db_column.column_name.lower()]

                            # TODO: DBeaverと同じようにオプションで変更可能にする
                            if column_value is None:
                                continue

                            # TODO: DBeaverと同じようにオプションで変更可能にする
                            xml_line += " " + db_column.column_name.upper() + '="'

                            if db_column.is_json():
                                column_value = str(column_value).replace("'", "&apos;")
                                column_value = column_value.replace('"', "&quot;")

                            if db_column.is_binary():
                                encoded = base64.b64encode(column_value)
                                column_value = encoded.decode("utf-8")

                            xml_line += str(column_value) + '"'

                        xml_line += "/>"
                        xml_lines.append(xml_line)

                    xml_lines.append('</dataset>')

                    xml_file_path_str = str(Path(xml_dir_path_str).joinpath(table_name_value+".xml"))

                    with open(xml_file_path_str, "w", encoding="utf-8") as file_obj:
                        file_obj.write("\n".join(xml_lines))
