from dataclasses import dataclass

from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.set_empty_str_instead_of_null import SetEmptyStrInsteadOfNull
from shared_code.domain.table.table_name.entity import TableName


@dataclass(frozen=True)
class OneTableDMLsBuildRequest:
    table_name: TableName
    db_columns: DBColumns
    data_range: list[list[str]]
    set_empty_str_instead_of_null: SetEmptyStrInsteadOfNull
