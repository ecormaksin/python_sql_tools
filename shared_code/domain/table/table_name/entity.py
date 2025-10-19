from dataclasses import dataclass


@dataclass(frozen=True)
class TableName:
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("TableName must be specified.")

    def __eq__(self, other):
        if not isinstance(other, TableName):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"TableName(value='{self.value}')"

    def can_replace_xlsx_sheet_name(self) -> bool:
        return True if len(self.value) <= 31 else False

    def cannot_replace_xlsx_sheet_name(self) -> bool:
        return not self.can_replace_xlsx_sheet_name()