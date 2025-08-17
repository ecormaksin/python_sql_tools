import os
from typing import Any, Optional

from shared_code.application.app_config.validation.cell_position_validator import (
    CellPositionValidator,
)
from shared_code.application.app_config.validation.request import (
    AppConfigValidationRequest as ValidationRequest,
)
from shared_code.application.app_config.validation.required_property_validator import (
    RequiredPropertyValidator,
)
from shared_code.application.app_config.validation.result_flag import (
    AppConfigValidationResultFlag as ValidationResultFlag,
)
from shared_code.domain.app_config import AppConfig
from shared_code.domain.cell_position import CellPosition
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.row_number import RowNumber
from shared_code.domain.table_name_definition_type import TableNameDefinitionType


class AppConfigFactory:

    def __init__(self, config_data: dict[str, Any]):
        self.__config_data = config_data
        self.__error_messages: list[str] = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> AppConfig:
        table_name_definition_type: TableNameDefinitionType = self.__get_table_name_definition_type()

        table_name_cell_position = None
        if table_name_definition_type == TableNameDefinitionType.CELL:
            table_name_cell_position = self.__get_cell_position(property_name="table_name_cell")

        db_column_name_row_number = self.__get_row_number(property_name="column_name_row")
        data_type_row_number = self.__get_row_number(property_name="data_type_row")
        data_start_cell_position = self.__get_cell_position(property_name="data_start_cell")
        number_of_lines_per_file = self.__get_number_of_lines_per_file()

        if len(self.__error_messages):
            raise RuntimeError(os.linesep.join(self.__error_messages))

        return AppConfig(table_name_definition_type=table_name_definition_type,
                table_name_cell_position=table_name_cell_position,
                db_column_name_row_number=db_column_name_row_number,
                data_type_row_number=data_type_row_number,
                data_start_cell_position=data_start_cell_position,
                number_of_lines_per_file=number_of_lines_per_file)

    def __validate_required_property(self, property_name: str) -> ValidationResultFlag:
        a_request = ValidationRequest(config_data=self.__config_data, property_name=property_name, error_messages=self.__error_messages)
        a_result = RequiredPropertyValidator.execute(a_request=a_request)

        self.__error_messages = a_result.error_messages
        return a_result.flag

    def __validate_cell_position(self, property_name: str) -> ValidationResultFlag:
        a_request = ValidationRequest(config_data=self.__config_data[property_name], property_name=property_name, error_messages=self.__error_messages)
        a_result = CellPositionValidator.execute(a_request=a_request)

        self.__error_messages = a_result.error_messages
        return a_result.flag

    def __get_table_name_definition_type(self) -> Optional[TableNameDefinitionType]:
        config_data = self.__config_data
        property_name = "table_name"

        result_flag = self.__validate_required_property(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        try:
            table_name_definition_type = TableNameDefinitionType.of(config_data[property_name])
            return table_name_definition_type
        except KeyError:
            self.__error_messages.append(f"The property '{property_name}' must be specified with one of the following values: sheet, cell.")
            return None

    def __get_cell_position(self, property_name: str) -> Optional[CellPosition]:
        result_flag = self.__validate_required_property(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        result_flag = self.__validate_cell_position(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        table_name_cell = self.__config_data[property_name]

        try:
            return CellPosition(row=int(table_name_cell["row"]), column=int(table_name_cell["column"]))
        except ValueError as exp:
            self.__error_messages.append(str(exp))
            return None

    def __get_row_number(self, property_name: str) -> Optional[RowNumber]:
        result_flag = self.__validate_required_property(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        try:
            return RowNumber(value=int(self.__config_data[property_name]))
        except ValueError as exp:
            self.__error_messages.append(str(exp))
            return None

    def __get_number_of_lines_per_file(self) -> Optional[NumberOfLinesPerFile]:
        number_of_lines_per_file = self.__config_data.get("number_of_lines_per_file", str(NumberOfLinesPerFile.UNLIMITED))

        try:
            return NumberOfLinesPerFile(value=int(number_of_lines_per_file))
        except ValueError as exp:
            self.__error_messages.append(str(exp))
            return None
