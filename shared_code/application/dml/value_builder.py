import re

from shared_code.application.dml.value_build_request import DMLValueBuildRequest
from shared_code.application.dml.value_quotation_getter import ValueQuotationGetter
from shared_code.application.dml.value_unicode_prefix_getter import (
    ValueUnicodePrefixGetter,
)
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag


class DMLValueBuilder:
    @classmethod
    def execute(cls, a_request: DMLValueBuildRequest) -> str:
        db_column = a_request.db_column
        cell_value = a_request.cell_value
        set_empty_str_instead_of_null = a_request.set_empty_str_instead_of_null

        column_default = db_column.column_default
        nullable_column_flag = db_column.nullable_column_flag
        data_type = db_column.data_type

        column_value = cell_value

        if not cell_value or cell_value == "None":
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

        dml_value = ""
        dml_value += unicode_prefix
        dml_value += value_quotation
        if no_quotation:
            dml_value += column_value
        else:
            dml_value += re.sub(r"'", "''", column_value)
        dml_value += value_quotation

        return dml_value