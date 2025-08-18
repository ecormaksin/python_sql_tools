from dataclasses import dataclass

from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class InsertDMLFirstPartCreationRequest:
    table_name: TableName
    db_columns: DBColumns


class InsertDMLFirstPartCreator:
    @classmethod
    def execute(cls, a_request: InsertDMLFirstPartCreationRequest) -> str:
        table_name = a_request.table_name
        db_columns = a_request.db_columns

        dml = f"INSERT INTO {table_name.value} ("
        for index, db_column in enumerate(db_columns.unmodifiable_elements):
            if index > 0:
                dml += ", "
            dml += db_column.column_name.value
        dml += ") VALUES ("

        return dml
