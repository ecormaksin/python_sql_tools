from dataclasses import dataclass


@dataclass(frozen=True)
class DMLs:
    value: list[str]
