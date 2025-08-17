from dataclasses import dataclass


@dataclass(frozen=True)
class CellPosition:
    row: int
    column: int

    def __post_init__(self):
        if type(self.row) is not int or \
                type(self.column) is not int or \
                self.row < 1 or \
                self.column < 1:
            raise ValueError("The row and column in CellPosition must be greater than equals 1.")

    def __eq__(self, other):
        if not isinstance(other, CellPosition):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        return f"CellPosition(row={str(self.row)}, column={str(self.column)})"
