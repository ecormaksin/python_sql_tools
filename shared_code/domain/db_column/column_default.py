from dataclasses import dataclass


@dataclass(frozen=True)
class ColumnDefault:
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("ColumnDefault must be specified.")

    def __eq__(self, other):
        if not isinstance(other, ColumnDefault):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"ColumnDefault(value='{self.value}')"
