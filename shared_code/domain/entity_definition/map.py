from dataclasses import dataclass
from typing import Optional

from shared_code.domain.entity_definition.entity import EntityDefinition
from shared_code.domain.table.table_name.entity import TableName


@dataclass(frozen=True)
class EntityDefinitions:
    elements: dict[TableName, EntityDefinition]

    @classmethod
    def empty(cls) -> "EntityDefinitions":
        return cls(elements=dict())

    def put(self, key: TableName, value: EntityDefinition) -> "EntityDefinitions":
        copied = dict(self.elements)
        copied[key] = value
        return self.__class__(elements=copied)

    def get(self, key: TableName) -> Optional[EntityDefinition]:
        return self.elements.get(key)

    def contains(self, key: TableName) -> bool:
        return True if self.get(key) else False

    def not_contains(self, key: TableName) -> bool:
        return not self.contains(key=key)

    @property
    def unmodifiable_elements(self) -> dict[TableName, EntityDefinition]:
        return dict(self.elements)
