from dataclasses import dataclass

from shared_code.application.app_config.validation.result_flag import AppConfigValidationResultFlag as ResultFlag


@dataclass(frozen=True)
class AppConfigValidationResult:
    flag: ResultFlag
    error_messages: list[str]
