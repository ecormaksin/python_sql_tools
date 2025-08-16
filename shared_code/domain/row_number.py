from dataclasses import dataclass

@dataclass(frozen=True)
class RowNumber:
    value: int