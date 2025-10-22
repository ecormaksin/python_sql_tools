from dataclasses import dataclass

from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema


@dataclass(frozen=True)
class TableNameWithSchemaSet:
    elements: set[TableNameWithSchema]

    @classmethod
    def empty(cls) -> "TableNameWithSchemaSet":
        return cls(elements=set())

    def is_empty(self) -> bool:
        return False if len(self.elements) else True

    def is_not_empty(self) -> bool:
        return not self.is_empty()

    def len(self) -> int:
        return len(self.elements)

    def put(self, element: TableNameWithSchema) -> "TableNameWithSchemaSet":
        copied = set(self.elements)
        copied.add(element)
        return self.__class__(elements=copied)

    def union(self, other: "TableNameWithSchemaSet") -> "TableNameWithSchemaSet":
        copied = set(self.elements)
        copied = copied.union(other.elements)
        return self.__class__(elements=copied)

    def remove(self, element: TableNameWithSchema) -> "TableNameWithSchemaSet":
        copied = set(self.elements)
        copied.remove(element)
        return self.__class__(elements=copied)

    def contains(self, element: TableNameWithSchema) -> bool:
        return True if element in self.elements else False

    def unmodified_elements(self) -> set[TableNameWithSchema]:
        return set(self.elements)
