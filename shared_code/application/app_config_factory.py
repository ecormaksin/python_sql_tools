from shared_code.domain.app_config import AppConfig
from shared_code.domain.cell_position import CellPosition
from shared_code.domain.table_name_definition_type import TableNameDefinitionType


from typing import Union, Optional

class AppConfigFactory:

    def __init__(self, config_data: dict[str, Union[str, int, dict[str, int]]]):
        self.__config_data = config_data
        self.__error_messages: list[str] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> AppConfig:
        config_data = self.__config_data

        self.__validate_required_properties()
        table_name_definition_type = self.__get_table_name_definition_type()

        table_name_cell_position = None
        if table_name_definition_type == TableNameDefinitionType.CELL:
            if "table_name_cell" not in config_data:
                raise RuntimeError("If you specify table name on cells, the 'table_name_cell' property must exists.")

            table_name_cell = config_data["table_name_cell"]

            if "row" not in table_name_cell or "column" not in table_name_cell:
                raise RuntimeError("The 'row' and 'column' properties must exists in the 'table_name_cell' property.")

            table_name_cell_position = CellPosition(row=int(table_name_cell["row"]), column=int(table_name_cell["column"]))

    def __validate_required_properties(self):
        config_data = self.__config_data

        required_properties: list[str] = ["table_name", "col_name_row", "data_type_row", "data_start_cell"]

        for required_property in required_properties:
            self.__validate_required_property(property_name=required_property)

    def __validate_required_property(self, property_name: str) -> bool:
        config_data = self.__config_data

        if property_name not in config_data:
            self.__error_messages.append(f"The property '{property_name}' must exists.")
            return False

        return True

    def __get_table_name_definition_type(self) -> Optional[TableNameDefinitionType]:
        config_data = self.__config_data
        try:
            table_name_definition_type = TableNameDefinitionType.of(config_data["table_name"])
            return table_name_definition_type
        except KeyError:
            self.__error_messages.append("The property 'table_name' must be specified with one of the following values: sheet, cell.")
            return None

    def __get_table_name_cell_position(self) -> Optional[CellPosition]:
        config_data = self.__config_data

        result = self.__validate_required_property(property_name="table_name_cell")
        if not result:
            return None

        table_name_cell = config_data["table_name_cell"]

        if "row" not in table_name_cell or "column" not in table_name_cell:
            raise RuntimeError("The 'row' and 'column' properties must exists in the 'table_name_cell' property.")

        return CellPosition(row=int(table_name_cell["row"]), column=int(table_name_cell["column"]))
