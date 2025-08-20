from shared_code.application.dml.dmls_builder import DMLsBuildRequest
from shared_code.application.dml.insert.first_part_builder import (
    InsertDMLFirstPartBuilder as FirstPartBuilder,
    InsertDMLFirstPartBuildRequest as FirstPartBuildRequest,
)
from shared_code.application.dml.value_quotation_getter import ValueQuotationGetter
from shared_code.application.dml.value_unicode_prefix_getter import (
    ValueUnicodePrefixGetter,
)


class InsertDMLsBuilder:
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

        first_part = FirstPartBuilder.execute(
            a_request=FirstPartBuildRequest(
                table_name=table_name, db_columns=db_columns
            )
        )

        dmls = []
        for row_data in a_request.data_range:
            dml = first_part

            for index, col_data in enumerate(row_data):
                db_column = db_columns.unmodifiable_elements[index]
                data_type = db_column.data_type
                no_quotation = db_column.no_quotation
                unicode_prefix = ValueUnicodePrefixGetter.execute(
                    data_type=data_type, no_quotation=no_quotation
                )
                value_quotation = ValueQuotationGetter.execute(
                    data_type=data_type, no_quotation=no_quotation
                )

                dml += ", " if index > 0 else ""
                dml += unicode_prefix
                dml += value_quotation
                dml += col_data
                dml += value_quotation

            dml += ");"
            dmls.append(dml)

        return dmls
