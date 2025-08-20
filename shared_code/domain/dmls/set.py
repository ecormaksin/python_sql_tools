from dataclasses import dataclass

from shared_code.domain.dmls.entity import DMLs
from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class DMLsSet:
    elements: dict[TableName, DMLs]

    @classmethod
    def empty(cls) -> "DMLsSet":
        return cls(elements={})

    def append(self, key: TableName, element: DMLs) -> "DMLsSet":
        copied = dict(self.elements)
        copied |= {key: element}
        return self.__class__(elements=copied)

    @property
    def unmodifiable_elements(self) -> dict[TableName, DMLs]:
        return dict(self.elements)
