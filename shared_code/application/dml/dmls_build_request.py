from dataclasses import dataclass

from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class DMLsBuildRequest:
    table_name: TableName
    db_columns: DBColumns
    data_range: list[list[str]]
