from dataclasses import dataclass


from shared_code.application.dml.insert.list_builder import InsertDMLsBuilder
from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class DMLsBuildRequest:
    table_name: TableName
    db_columns: DBColumns
    data_range: list[list[str]]


class DMLsBuilder:
    def __init__(self, a_request: DMLsBuildRequest):
        self.__a_request = a_request

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> list[str]:
        a_request = self.__a_request

        with InsertDMLsBuilder(a_request=a_request) as insert_dmls_builder:
            return insert_dmls_builder.execute()
