from typing import Optional
from dataclasses import dataclass

from shared_code.application.app_config.builder.base.builder import AbstractBuilder
from shared_code.application.app_config.builder.base.request import BaseBuildRequest
from shared_code.application.app_config.builder.base.result import (
    AbstractBuildResult,
)

from shared_code.application.app_config.builder.required_property_flag import (
    RequiredPropertyFlag,
)
from shared_code.domain.row_number import RowNumber
from shared_code.application.app_config.validation.result_flag import (
    AppConfigValidationResultFlag as ValidationResultFlag,
)


@dataclass(frozen=True)
class RowNumberBuildRequest(BaseBuildRequest):
    property_name: str
    is_required: RequiredPropertyFlag


@dataclass(frozen=True)
class RowNumberBuildResult(AbstractBuildResult):
    row_number: Optional[RowNumber]


BuildRequest = RowNumberBuildRequest
BuildResult = RowNumberBuildResult


class RowNumberBuilder(AbstractBuilder):
    def __init__(self, a_request: BuildRequest):
        super().__init__(a_request=a_request)
        self.__property_name = a_request.property_name
        self.__is_required = a_request.is_required

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> BuildResult:
        row_number = self.__get_row_number()

        return BuildResult(
            row_number=row_number,
            error_messages=super().error_messages,
        )

    def __get_row_number(self) -> Optional[RowNumber]:
        property_name = self.__property_name
        is_required = self.__is_required

        if is_required == RequiredPropertyFlag.YES:
            result_flag = super().validate_required_property(
                property_name=property_name
            )
            if result_flag == ValidationResultFlag.NG:
                return None
        else:
            if property_name not in super().config_data:
                return None

        try:
            return RowNumber(value=int(super().config_data[property_name]))
        except ValueError as exp:
            error_messages = super().error_messages
            error_messages.append(str(exp))
            super().replace_error_messages(error_messages=error_messages)
            return None
