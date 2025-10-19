from enum import Enum


class TableType(Enum):
    BASE_TABLE = (1, "BASE TABLE")
    VIEW = (2, "VIEW")

    @classmethod
    def from_mysql_value(cls, mysql_value: str):
        for member in cls:
            if member._mysql_value.lower() == mysql_value.lower():
                return member
        raise KeyError(f"'{mysql_value}' is not found.")

    def __init__(self, ddl_sort_order: int, mysql_value: str):
        self._ddl_sort_order = ddl_sort_order
        self._mysql_value = mysql_value

    @property
    def ddl_sort_order(self) -> int:
        return self._ddl_sort_order
