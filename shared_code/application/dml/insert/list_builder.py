from shared_code.application.dml.dml_build_request import DMLBuildRequest
from shared_code.application.dml.dmls_build_request import DMLsBuildRequest
from shared_code.application.dml.insert.first_part_builder import (
    InsertDMLFirstPartBuilder as FirstPartBuilder,
)
from shared_code.application.dml.insert.first_part_builder import (
    InsertDMLFirstPartBuildRequest as FirstPartBuildRequest,
)
from shared_code.application.dml.insert.values_clause_builder import (
    InsertValueClauseBuilder,
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
        set_empty_str_instead_of_null = a_request.set_empty_str_instead_of_null

        first_part = FirstPartBuilder.execute(
            a_request=FirstPartBuildRequest(
                table_name=table_name, db_columns=db_columns
            )
        )

        dmls = []
        for row_data in a_request.data_range:
            dml = first_part

            dml_build_request = DMLBuildRequest(
                table_name=table_name,
                db_columns=db_columns,
                row_data=row_data,
                set_empty_str_instead_of_null=set_empty_str_instead_of_null,
            )
            with InsertValueClauseBuilder(
                a_request=dml_build_request
            ) as insert_value_clause_builder:
                dml += insert_value_clause_builder.execute()

            dml += ");"
            dmls.append(dml)

        return dmls
