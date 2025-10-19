from dataclasses import dataclass

from shared_code.domain.table.table_type import TableType
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema
from shared_code.domain.table_name_with_schema.set import TableNameWithSchemaSet


@dataclass(frozen=True)
class TableDependency:
    table_name_with_schema: TableNameWithSchema
    table_type: TableType
    dependent_table_set: TableNameWithSchemaSet