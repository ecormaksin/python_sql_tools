from dataclasses import dataclass
from functools import total_ordering

from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName


@total_ordering
@dataclass(frozen=True)
class TableNameWithSchema:
    schema: Schema
    table_name: TableName

    def __eq__(self, other):
        if not isinstance(other, TableNameWithSchema):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __lt__(self, other):
        if not isinstance(other, TableNameWithSchema):
            return NotImplemented

        if self.schema < other.schema:
            return True

        return self.schema == other.schema and self.table_name < other.table_name
