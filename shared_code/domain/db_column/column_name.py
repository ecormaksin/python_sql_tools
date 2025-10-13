from dataclasses import dataclass


@dataclass(frozen=True)
class ColumnName:
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("ColumnName must be specified.")

    def __eq__(self, other):
        if not isinstance(other, ColumnName):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"ColumnName(value='{self.value}')"

    def lower(self) -> str:
        return self.value.lower()

    def upper(self) -> str:
        return self.value.upper()
