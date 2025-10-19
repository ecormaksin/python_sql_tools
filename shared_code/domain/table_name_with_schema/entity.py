from dataclasses import dataclass

from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName


@dataclass(frozen=True)
class TableNameWithSchema:
    schema: Schema
    table_name: TableName
