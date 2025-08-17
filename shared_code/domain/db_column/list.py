from dataclasses import dataclass

from shared_code.domain.db_column.entity import DBColumn


@dataclass(frozen=True)
class DBColumns:
    elements: list[DBColumn]

    @classmethod
    def empty(cls) -> "DBColumns":
        return cls(elements=list())

    def append(self, element: DBColumn) -> "DBColumns":
        copied = list(self.elements)
        copied.append(element)
        return self.__class__(elements=copied)

    @property
    def unmodifiable_elements(self) -> list[DBColumn]:
        return list(self.elements)
