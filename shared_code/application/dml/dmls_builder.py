from dataclasses import dataclass

from shared_code.application.dml.insert_dml_first_part_builder import (
    InsertDMLFirstPartBuilder,
    InsertDMLFirstPartBuildRequest,
)
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
        table_name = a_request.table_name
        db_columns = a_request.db_columns

        insert_dml_first_part = InsertDMLFirstPartBuilder.execute(
            a_request=InsertDMLFirstPartBuildRequest(
                table_name=table_name, db_columns=db_columns
            )
        )

        dmls = []
        for row_data in a_request.data_range:
            dml = insert_dml_first_part

            for index, col_data in enumerate(row_data):
                db_column = db_columns.unmodifiable_elements[index]
                data_type = db_column.data_type
                no_quotation = db_column.no_quotation
                do_add_quotation = data_type.do_add_quotation() and not no_quotation

                dml += ", " if index > 0 else ""
                dml += (
                    "N"
                    if data_type.do_add_unicode_prefix() and not no_quotation
                    else ""
                )

                dml += "'" if do_add_quotation else ""
                dml += col_data
                dml += "'" if do_add_quotation else ""

            dml += ");"
            dmls.append(dml)

        return dmls
