from shared_code.application.dml.dml_build_request import DMLBuildRequest
from shared_code.application.dml.dmls_build_request import DMLsBuildRequest
from shared_code.application.dml.insert.entity_builder import (
    InsertDMLBuilder,
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

        dmls = []
        for row_data in a_request.data_range:

            dml_build_request = DMLBuildRequest(
                table_name=table_name,
                db_columns=db_columns,
                row_data=row_data,
                set_empty_str_instead_of_null=set_empty_str_instead_of_null,
            )
            with InsertDMLBuilder(
                a_request=dml_build_request
            ) as insert_value_clause_builder:
                dml = insert_value_clause_builder.execute()

            dmls.append(dml)

        return dmls
