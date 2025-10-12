from dataclasses import dataclass
from typing import Optional

from shared_code.domain.table_name.entity import TableName


@dataclass(frozen=True)
class TableNameSet:
    elements: set[TableName]

    @classmethod
    def empty(cls) -> "TableNameSet":
        return cls(elements=set())

    @classmethod
    def from_csv_str(cls, csv_str: Optional[str]) -> "TableNameSet":
        if not csv_str:
            return cls.empty()

        set_obj = set()
        for element in csv_str.split(","):
            if not element:
                continue

            set_obj.add(TableName(value=element.strip()))

        return cls(elements=set_obj)

    def is_empty(self) -> bool:
        return False if len(self.elements) else True

    def put(self, element: TableName) -> "TableNameSet":
        copied = set(self.elements)
        copied.add(element)
        return self.__class__(elements=copied)

    def contains(self, element: TableName) -> bool:
        return True if element in self.elements else False

    def in_clause(self) -> str:
        table_list = []
        for element in self.elements:
            table_list.append(f"'{element.value}'")

        return ", ".join(table_list)

    def can_replace_xlsx_sheet_name(self) -> bool:
        for element in self.elements:
            if element.cannot_replace_xlsx_sheet_name():
                return False

        return True
