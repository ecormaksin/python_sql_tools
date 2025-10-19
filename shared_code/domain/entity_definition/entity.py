from dataclasses import dataclass

from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.table.table_name.entity import TableName


@dataclass(frozen=True)
class EntityDefinition:
    table_name: TableName
    db_columns: DBColumns

    def select_statement(self) -> str:
        query = "select "

        for index, db_column in enumerate(self.db_columns.unmodifiable_elements):
            if index > 0:
                query += ", "

            column_name = db_column.column_name.value
            query += column_name + " as " + column_name.lower()

        query += " from "
        query += self.table_name.value

        return query