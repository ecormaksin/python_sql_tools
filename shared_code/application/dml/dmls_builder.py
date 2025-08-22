from shared_code.application.dml.dmls_build_request import DMLsBuildRequest
from shared_code.application.dml.insert.list_builder import InsertDMLsBuilder


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
