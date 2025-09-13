from dataclasses import dataclass


@dataclass(frozen=True)
class KeyPosition:
    value: int

    @classmethod
    def from_str(cls, str_value: str) -> "KeyPosition":
        return cls(value=int(str_value))

    def __post_init__(self):
        if type(self.value) is not int or not self.value:
            raise ValueError("KeyPosition must be specified.")

    def __eq__(self, other):
        if not isinstance(other, KeyPosition):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"KeyPosition(value='{self.value}')"
