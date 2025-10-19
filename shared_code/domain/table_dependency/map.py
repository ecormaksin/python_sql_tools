from dataclasses import dataclass
from typing import Optional

from shared_code.domain.table_dependency.entity import TableDependency
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema


@dataclass(frozen=True)
class TableDependencyMap:
    elements: dict[TableNameWithSchema, TableDependency]

    @classmethod
    def empty(cls) -> "TableDependencyMap":
        return cls(elements=dict())

    def put(
        self, key: TableNameWithSchema, value: TableDependency
    ) -> "TableDependencyMap":
        copied = dict(self.elements)
        copied[key] = value
        return self.__class__(elements=copied)

    def get(self, key: TableNameWithSchema) -> Optional[TableDependency]:
        return self.elements.get(key)

    def contains(self, key: TableNameWithSchema) -> bool:
        return True if self.get(key) else False

    def not_contains(self, key: TableNameWithSchema) -> bool:
        return not self.contains(key=key)

    @property
    def unmodifiable_elements(self) -> dict[TableNameWithSchema, TableDependency]:
        return dict(self.elements)
