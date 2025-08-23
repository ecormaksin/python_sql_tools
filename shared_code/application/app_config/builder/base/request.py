from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BaseBuildRequest:
    config_data: dict[str, Any]
    error_messages: list[str]
