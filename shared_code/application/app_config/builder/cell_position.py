from typing import Optional
from dataclasses import dataclass

from shared_code.application.app_config.builder.base.builder import AbstractBuilder
from shared_code.application.app_config.builder.base.request import BaseBuildRequest
from shared_code.application.app_config.builder.base.result import (
    AbstractBuildResult,
)
from shared_code.application.app_config.validation.cell_position_validator import (
    CellPositionValidator,
)
from shared_code.domain.cell_position import CellPosition
from shared_code.application.app_config.validation.result_flag import (
    AppConfigValidationResultFlag as ValidationResultFlag,
)
from shared_code.application.app_config.validation.request import (
    AppConfigValidationRequest as ValidationRequest,
)


@dataclass(frozen=True)
class CellPositionBuildRequest(BaseBuildRequest):
    property_name: str


@dataclass(frozen=True)
class CellPositionBuildResult(AbstractBuildResult):
    cell_position: Optional[CellPosition]


BuildRequest = CellPositionBuildRequest
BuildResult = CellPositionBuildResult


class CellPositionBuilder(AbstractBuilder):
    def __init__(self, a_request: BuildRequest):
        super().__init__(a_request=a_request)
        self.__property_name = a_request.property_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> BuildResult:
        cell_position = self.__get_cell_position()

        return BuildResult(
            cell_position=cell_position,
            error_messages=super().error_messages,
        )

    def __validate_cell_position(self) -> ValidationResultFlag:
        property_name = self.__property_name
        a_request = ValidationRequest(
            config_data=super().config_data[property_name],
            property_name=property_name,
            error_messages=super().error_messages,
        )
        a_result = CellPositionValidator.execute(a_request=a_request)

        super().replace_error_messages(error_messages=a_result.error_messages)
        return a_result.flag

    def __get_cell_position(self) -> Optional[CellPosition]:
        property_name = self.__property_name
        result_flag = super().validate_required_property(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        result_flag = self.__validate_cell_position()
        if result_flag == ValidationResultFlag.NG:
            return None

        table_name_cell = super().config_data[property_name]

        try:
            return CellPosition(
                row=int(table_name_cell["row"]), column=int(table_name_cell["column"])
            )
        except ValueError as exp:
            error_messages = super().error_messages
            error_messages.append(str(exp))
            super().replace_error_messages(error_messages=error_messages)
            return None
