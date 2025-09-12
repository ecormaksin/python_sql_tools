from dataclasses import dataclass


@dataclass(frozen=True)
class SetEmptyStrInsteadOfNull:
    value: bool

    def __post_init__(self):
        if type(self.value) is not bool:
            raise ValueError("SetEmptyStrInsteadOfNull must be bool.")

    def __eq__(self, other):
        if not isinstance(other, SetEmptyStrInsteadOfNull):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"SetEmptyStrInsteadOfNull(value={str(self.value)})"

    def is_true(self) -> bool:
        return self.value

    def is_false(self) -> bool:
        return not self.is_true()
