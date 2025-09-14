from shared_code.application.dml.dml_build_request import DMLBuildRequest
from shared_code.application.dml.insert.entity_builder import (
    InsertDMLBuilder,
)
from shared_code.application.dml.one_table_dmls_build_request import (
    OneTableDMLsBuildRequest,
)


class InsertDMLListBuilder:
    @classmethod
    def execute(cls, a_request: OneTableDMLsBuildRequest) -> list[str]:
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
            dml = InsertDMLBuilder.execute(a_request=dml_build_request)

            dmls.append(dml)

        return dmls
