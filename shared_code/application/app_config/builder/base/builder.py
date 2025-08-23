from abc import ABC
from typing import Any

from shared_code.application.app_config.validation.required_property_validator import (
    RequiredPropertyValidator,
)
from shared_code.application.app_config.validation.result_flag import (
    AppConfigValidationResultFlag as ValidationResultFlag,
)
from shared_code.application.app_config.validation.request import (
    AppConfigValidationRequest as ValidationRequest,
)

from shared_code.application.app_config.builder.base.request import (
    BaseBuildRequest,
)
from shared_code.application.app_config.builder.base.result import (
    AbstractBuildResult,
)


class AbstractBuilder(ABC):
    def __init__(self, a_request: BaseBuildRequest):
        self.__config_data = a_request.config_data
        self.__error_messages = a_request.error_messages

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> AbstractBuildResult:
        raise NotImplementedError()

    def validate_required_property(self, property_name: str) -> ValidationResultFlag:
        a_request = ValidationRequest(
            config_data=self.__config_data,
            property_name=property_name,
            error_messages=self.__error_messages,
        )
        a_result = RequiredPropertyValidator.execute(a_request=a_request)

        self.__error_messages = a_result.error_messages
        return a_result.flag

    @property
    def config_data(self) -> dict[str, Any]:
        return self.__config_data

    @property
    def error_messages(self) -> list[str]:
        return self.__error_messages

    def replace_error_messages(self, error_messages: list[str]):
        self.__error_messages = error_messages
