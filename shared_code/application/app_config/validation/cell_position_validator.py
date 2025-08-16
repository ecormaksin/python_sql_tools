
from shared_code.application.app_config.validation.request import AppConfigValidationRequest as Request
from shared_code.application.app_config.validation.result import AppConfigValidationResult as Result
from shared_code.application.app_config.validation.result_flag import AppConfigValidationResultFlag as ResultFlag


class CellPositionValidator:
    @classmethod
    def execute(cls, a_request: Request) -> Result:
        config_data = a_request.config_data
        property_name = a_request.property_name
        error_messages = list(a_request.error_messages)

        if "row" in config_data and "column" in config_data:
            flag = ResultFlag.OK
        else:
            error_messages.append(f"The 'row' and 'column' properties must exist in the '{property_name}' property.")
            flag = ResultFlag.NG

        return Result(flag=flag, error_messages=error_messages)
