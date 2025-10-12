from dataclasses import dataclass

from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.table_name.entity import TableName


@dataclass(frozen=True)
class EntityDefinition:
    table_name: TableName
    db_columns: DBColumns