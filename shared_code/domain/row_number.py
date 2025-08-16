from dataclasses import dataclass


@dataclass(frozen=True)
class RowNumber:
    value: int

    def __eq__(self, other):
        if not isinstance(other, RowNumber):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"RowNumber(value={str(self.value)})"