from dataclasses import dataclass

@dataclass(frozen=True)
class CellPosition:
    row: int
    column: int