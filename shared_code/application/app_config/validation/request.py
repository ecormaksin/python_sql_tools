from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class AppConfigValidationRequest:
    config_data: dict[str, Any]
    property_name: str
    error_messages: list[str]
    