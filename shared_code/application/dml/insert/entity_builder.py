from shared_code.application.dml.dml_build_request import DMLBuildRequest
from shared_code.application.dml.insert.first_part_builder import (
    InsertDMLFirstPartBuilder as FirstPartBuilder,
)
from shared_code.application.dml.insert.first_part_builder import (
    InsertDMLFirstPartBuildRequest as FirstPartBuildRequest,
)
from shared_code.application.dml.value_build_request import DMLValueBuildRequest
from shared_code.application.dml.value_builder import DMLValueBuilder


class InsertDMLBuilder:
    @classmethod
    def execute(cls, a_request: DMLBuildRequest) -> str:
        table_name = a_request.table_name
        db_columns = a_request.db_columns
        row_data = a_request.row_data
        set_empty_str_instead_of_null = a_request.set_empty_str_instead_of_null

        first_part = FirstPartBuilder.execute(
            a_request=FirstPartBuildRequest(
                table_name=table_name, db_columns=db_columns
            )
        )

        db_columns_size = len(db_columns.unmodifiable_elements)

        dml = first_part

        dml_values = []
        for index, cell_value in enumerate(row_data):
            if index >= db_columns_size:
                continue

            db_column = db_columns.unmodifiable_elements[index]

            dml_value = DMLValueBuilder.execute(
                a_request=DMLValueBuildRequest(
                    db_column=db_column,
                    cell_value=cell_value,
                    set_empty_str_instead_of_null=set_empty_str_instead_of_null,
                )
            )

            dml_values.append(dml_value)

        dml += ", ".join(dml_values)
        dml += ");"

        return dml

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """
