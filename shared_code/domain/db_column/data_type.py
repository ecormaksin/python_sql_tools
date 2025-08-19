from dataclasses import dataclass


@dataclass(frozen=True)
class DataType:
    QUOTATION_TARGET = {"VARCHAR", "CHAR", "DATE", "DATETIME"}

    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("DataType must be specified.")

    def __eq__(self, other):
        if not isinstance(other, DataType):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"DataType(value='{self.value}')"

    def do_add_quotation(self) -> bool:
        a_value = self.value
        index = a_value.find("(")
        data_type_part = a_value if index == -1 else a_value[:index]
