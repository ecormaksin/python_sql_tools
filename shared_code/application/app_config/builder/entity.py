import os
from typing import Any, Optional

from shared_code.application.app_config.builder.cell_position import (
    CellPositionBuildRequest,
    CellPositionBuilder,
)
from shared_code.application.app_config.builder.required_property_flag import (
    RequiredPropertyFlag,
)
from shared_code.application.app_config.builder.row_number import (
    RowNumberBuildRequest,
    RowNumberBuilder,
)
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
from shared_code.domain.sheet_names.exclude import ExcludeSheetNames
from shared_code.domain.sheet_names.target import TargetSheetNames


class AppConfigBuilder:
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
        config_data = self.__config_data

        table_name_cell_position = self.__get_cell_position(property_name="table_name_cell")
        db_column_name_row_number = self.__get_required_row_number(
            property_name="column_name_row"
        )
        data_type_row_number = self.__get_required_row_number(
            property_name="data_type_row"
        )
        key_position_row_number = self.__get_optional_row_number(
            property_name="key_position_row"
        )
        no_quotation_row_number = self.__get_optional_row_number(
            property_name="no_quotation_row"
        )
        data_start_cell_position = self.__get_cell_position(
            property_name="data_start_cell"
        )
        number_of_lines_per_file = self.__get_number_of_lines_per_file()
        target_sheet_names = TargetSheetNames(config_data.get("target_sheet_names", ""))
        exclude_sheet_names = ExcludeSheetNames(
            config_data.get("exclude_sheet_names", "")
        )
        if target_sheet_names.overlapped(exclude_sheet_names):
            self.__error_messages.append(
                "The same sheet names are specified in 'target_sheet_names' and 'exclude_sheet_names'."
            )

        if len(self.__error_messages):
            raise RuntimeError(os.linesep.join(self.__error_messages))

        return AppConfig(
            target_sheet_names=target_sheet_names,
            exclude_sheet_names=exclude_sheet_names,
            table_name_cell_position=table_name_cell_position,
            db_column_name_row_number=db_column_name_row_number,
            data_type_row_number=data_type_row_number,
            key_position_row_number=key_position_row_number,
            no_quotation_row_number=no_quotation_row_number,
            data_start_cell_position=data_start_cell_position,
            number_of_lines_per_file=number_of_lines_per_file,
        )

    def __validate_required_property(self, property_name: str) -> ValidationResultFlag:
        a_request = ValidationRequest(
            config_data=self.__config_data,
            property_name=property_name,
            error_messages=self.__error_messages,
        )
        a_result = RequiredPropertyValidator.execute(a_request=a_request)

        self.__error_messages = a_result.error_messages
        return a_result.flag

    def __validate_cell_position(self, property_name: str) -> ValidationResultFlag:
        a_request = ValidationRequest(
            config_data=self.__config_data[property_name],
            property_name=property_name,
            error_messages=self.__error_messages,
        )
        a_result = CellPositionValidator.execute(a_request=a_request)

        self.__error_messages = a_result.error_messages
        return a_result.flag

    def __get_cell_position(self, property_name: str) -> Optional[CellPosition]:
        a_request = CellPositionBuildRequest(
            config_data=self.__config_data,
            error_messages=self.__error_messages,
            property_name=property_name,
        )
        with CellPositionBuilder(a_request=a_request) as a_builder:
            a_result = a_builder.execute()

        self.__error_messages = a_result.error_messages
        return a_result.cell_position

    def __get_required_row_number(self, property_name: str) -> Optional[RowNumber]:
        return self.__get_row_number(
            property_name=property_name, is_required=RequiredPropertyFlag.YES
        )

    def __get_optional_row_number(self, property_name: str) -> Optional[RowNumber]:
        return self.__get_row_number(
            property_name=property_name, is_required=RequiredPropertyFlag.NO
        )

    def __get_row_number(
        self,
        property_name: str,
        is_required: RequiredPropertyFlag,
    ) -> Optional[RowNumber]:
        a_request = RowNumberBuildRequest(
            config_data=self.__config_data,
            error_messages=self.__error_messages,
            property_name=property_name,
            is_required=is_required,
        )
        with RowNumberBuilder(a_request=a_request) as a_builder:
            a_result = a_builder.execute()

        self.__error_messages = a_result.error_messages
        return a_result.row_number

    def __get_number_of_lines_per_file(self) -> Optional[NumberOfLinesPerFile]:
        number_of_lines_per_file = self.__config_data.get(
            "number_of_lines_per_file", str(NumberOfLinesPerFile.UNLIMITED)
        )

        try:
            return NumberOfLinesPerFile(value=int(number_of_lines_per_file))
        except ValueError as exp:
            self.__error_messages.append(str(exp))
            return None
