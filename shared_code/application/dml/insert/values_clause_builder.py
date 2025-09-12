import re
from typing import Optional

from shared_code.application.dml.dml_build_request import DMLBuildRequest
from shared_code.application.dml.value_quotation_getter import ValueQuotationGetter
from shared_code.application.dml.value_unicode_prefix_getter import (
    ValueUnicodePrefixGetter,
)
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag


class InsertValueClauseBuilder:
    def __init__(self, a_request: DMLBuildRequest):
        self.__a_request = a_request

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> str:
        a_request = self.__a_request
        db_columns = a_request.db_columns
        row_data = a_request.row_data

        db_columns_size = len(db_columns.unmodifiable_elements)

        value_clause = ""

        for index, col_data in enumerate(row_data):
            if index >= db_columns_size:
                continue

            db_column = db_columns.unmodifiable_elements[index]

            value_clause += ", " if index > 0 else ""

            value_clause += self.__return_value_part(
                db_column=db_column, col_data=col_data
            )

        return value_clause

    def __return_value_part(self, db_column: DBColumn, col_data: Optional[str]) -> str:
        a_request = self.__a_request
        set_empty_str_instead_of_null = a_request.set_empty_str_instead_of_null

        column_default = db_column.column_default
        nullable_column_flag = db_column.nullable_column_flag
        data_type = db_column.data_type

        column_value = col_data

        if not col_data or col_data == "None":
            if not column_default:
                if data_type.do_not_add_quotation():
                    return "null"

                if (
                    nullable_column_flag == NullableColumnFlag.YES
                    and set_empty_str_instead_of_null.is_false()
                ):
                    return "null"

                column_value = ""
            else:
                column_value = column_default.value

        no_quotation = db_column.no_quotation
        unicode_prefix = ValueUnicodePrefixGetter.execute(
            data_type=data_type, no_quotation=no_quotation
        )
        value_quotation = ValueQuotationGetter.execute(
            data_type=data_type, no_quotation=no_quotation
        )

        value_part = ""
        value_part += unicode_prefix
        value_part += value_quotation
        if no_quotation:
            value_part += column_value
        else:
            value_part += re.sub(r"'", "''", column_value)
        value_part += value_quotation

        return value_part
