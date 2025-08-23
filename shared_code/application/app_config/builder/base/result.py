from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class AbstractBuildResult(ABC):
    error_messages: list[str]
