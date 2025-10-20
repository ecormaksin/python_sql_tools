from dataclasses import dataclass
from functools import total_ordering

from shared_code.domain.table.table_type import TableType
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema
from shared_code.domain.table_name_with_schema.set import TableNameWithSchemaSet


@total_ordering
@dataclass(frozen=True)
class TableDependency:
    table_name_with_schema: TableNameWithSchema
    table_type: TableType
    dependent_table_set: TableNameWithSchemaSet

    def __eq__(self, other):
        if not isinstance(other, TableDependency):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __lt__(self, other):
        if not isinstance(other, TableDependency):
            return NotImplemented

        if self.table_type.ddl_sort_order < other.table_type.ddl_sort_order:
            return True

        if (
            self.table_type.ddl_sort_order == other.table_type.ddl_sort_order
            and self.dependent_table_set.len() < other.dependent_table_set.len()
        ):
            return True

        return self.table_name_with_schema < other.table_name_with_schema

    def update_dependent_table_set(
        self, dependent_table_set: TableNameWithSchemaSet
    ) -> "TableDependency":
        return self.__class__(
            self.table_name_with_schema, self.table_type, dependent_table_set
        )