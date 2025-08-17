from dataclasses import dataclass


@dataclass(frozen=True)
class NumberOfLinesPerFile:
    UNLIMITED = -1

    value: int

    def __post_init__(self):
        if type(self.value) is not int or self.value < NumberOfLinesPerFile.UNLIMITED:
            raise ValueError(f"NumberOfLinesPerFile must be greater than equals {str(NumberOfLinesPerFile.UNLIMITED)}.")

    def __eq__(self, other):
        if not isinstance(other, NumberOfLinesPerFile):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"NumberOfLinesPerFile(value={str(self.value)})"