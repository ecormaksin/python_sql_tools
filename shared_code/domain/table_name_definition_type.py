from enum import StrEnum


class TableNameDefinitionType(StrEnum):
    SHEET = "sheet"
    CELL = "cell"

    @classmethod
    def of(cls, key: str):
        for member in cls:
            if member.value == key.lower():
                return member
        raise KeyError(f"The key {key} is not defined.")

    def __repr__(self):
        return f"TableNameDefinitionType('{self.value}')"
    