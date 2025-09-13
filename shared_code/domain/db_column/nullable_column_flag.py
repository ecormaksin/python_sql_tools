from enum import StrEnum, auto


class NullableColumnFlag(StrEnum):
    YES = auto()
    NO = auto()

    @classmethod
    def from_str(cls, key: str):
        for member in cls:
            if member.value.lower() == key.lower():
                return member
        raise KeyError(f"The key {key} is not defined.")

    def __repr__(self):
        return f"NullableColumnFlag('{self.value}')"
