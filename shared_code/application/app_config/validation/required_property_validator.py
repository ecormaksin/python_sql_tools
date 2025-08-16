
from shared_code.application.app_config.validation.request import AppConfigValidationRequest as Request
from shared_code.application.app_config.validation.result import AppConfigValidationResult as Result
from shared_code.application.app_config.validation.result_flag import AppConfigValidationResultFlag as ResultFlag


class RequiredPropertyValidator:
    @classmethod
    def execute(cls, a_request: Request) -> Result:
        property_name = a_request.property_name
        error_messages = list(a_request.error_messages)

        if property_name in a_request.config_data:
            flag = ResultFlag.OK
        else:
            error_messages.append(f"The property '{property_name}' must exists.")
            flag = ResultFlag.NG

        return Result(flag=flag, error_messages=error_messages)
