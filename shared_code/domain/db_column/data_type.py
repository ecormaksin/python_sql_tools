from dataclasses import dataclass


@dataclass(frozen=True)
class DataType:
    QUOTATION_TARGET = {
        "BINARY",
        "BLOB",
        "BPCHAR",
        "CHAR",
        "CHARACTER",
        "CLOB",
        "DATE",
        "DATETIME",
        "ENUM",
        "INTERVAL",
        "JSON",
        "MACADDR ",
        "MACADDR8",
        "NCHAR",
        "NTEXT",
        "NVARCHAR",
        "NVARCHAR2",
        "SET",
        "SMALLDATETIME",
        "TEXT",
        "TIME",
        "TIMESTAMP",
        "VARBINARY",
        "VARCHAR",
        "VARCHAR2",
        "YEAR",
    }
    ADD_UNICODE_PREFIX = {
        "NCHAR",
        "NTEXT",
        "NVARCHAR",
        "NVARCHAR2",
    }

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
        data_type_part = DataType.__convert_for_comparison(a_value=a_value)
        return data_type_part in self.QUOTATION_TARGET

    def do_not_add_quotation(self) -> bool:
        return not self.do_add_quotation()

    def do_add_unicode_prefix(self) -> bool:
        a_value = self.value
        data_type_part = DataType.__convert_for_comparison(a_value=a_value)
        return data_type_part in self.ADD_UNICODE_PREFIX

    def is_json(self) -> bool:
        return True if self.value.lower() == "json" else False

    def is_binary(self) -> bool:
        return True if "binary" in self.value.lower() else False

    @staticmethod
    def __convert_for_comparison(a_value: str) -> str:
        data_type_part = a_value.lstrip("@")  # A5:SQLの型ドメイン対応

        for target_character in ["(", " "]:
            data_type_part = DataType.__cut_value(
                a_value=data_type_part, target_character=target_character
            )

        return data_type_part.upper()

    @staticmethod
    def __cut_value(a_value: str, target_character: str) -> str:
        index = a_value.find(target_character)
        value_part = a_value if index == -1 else a_value[:index]
        return value_part
