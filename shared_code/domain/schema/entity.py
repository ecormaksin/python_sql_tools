from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Schema:
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("Schema must be specified.")

    def __eq__(self, other):
        if not isinstance(other, Schema):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        if not isinstance(other, Schema):
            return NotImplemented

        return self.value < other.value

    def __repr__(self):
        return f"Schema(value='{self.value}')"

