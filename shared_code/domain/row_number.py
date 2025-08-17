from dataclasses import dataclass


@dataclass(frozen=True)
class RowNumber:
    value: int

    def __post_init__(self):
        if type(self.value) is not int or self.value < 1:
            raise ValueError("RowNumber must be greater than equals 1.")

    def __eq__(self, other):
        if not isinstance(other, RowNumber):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"RowNumber(value={str(self.value)})"