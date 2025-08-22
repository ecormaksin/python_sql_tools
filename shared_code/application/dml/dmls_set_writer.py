from dataclasses import dataclass


from shared_code.domain.dmls.set import DMLsSet
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath


@dataclass(frozen=True)
class DMLsSetBuildRequest:
    sink_dml_dir_path: SinkDMLDirectoryPath
    dmls_set: DMLsSet
    number_of_lines_per_file: NumberOfLinesPerFile


class DMLsSetWriter:
    def __init__(self, a_request: DMLsSetBuildRequest):
        self.__a_request = a_request

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self):
        a_request = self.__a_request
