from shared_code.application.dml.insert.list_builder import InsertDMLListBuilder
from shared_code.application.dml.one_table_dmls_build_request import (
    OneTableDMLsBuildRequest,
)


class OneTableDMLsBuilder:
    @classmethod
    def execute(cls, a_request: OneTableDMLsBuildRequest) -> list[str]:
        return InsertDMLListBuilder.execute(a_request=a_request)
