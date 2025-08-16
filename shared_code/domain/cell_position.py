from dataclasses import dataclass


@dataclass(frozen=True)
class CellPosition:
    row: int
    column: int

    def __repr__(self):
        return f"CellPosition(row={str(self.row)}, column={str(self.column)})"

    def __eq__(self, other):
        if not isinstance(other, CellPosition):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))