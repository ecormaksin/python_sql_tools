from dataclasses import dataclass

from shared_code.application.dml.dmls_writer import DMLsWriteRequest, DMLsWriter
from shared_code.domain.dmls.set import DMLsSet
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath


@dataclass(frozen=True)
class DMLsSetWriteRequest:
    sink_dml_dir_path: SinkDMLDirectoryPath
    dmls_set: DMLsSet
    number_of_lines_per_file: NumberOfLinesPerFile


class DMLsSetWriter:
    def __init__(self, a_request: DMLsSetWriteRequest):
        self.__a_request = a_request

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self):
        a_request = self.__a_request
        sink_dml_dir_path = a_request.sink_dml_dir_path
        dmls_set = a_request.dmls_set
        number_of_lines_per_file = a_request.number_of_lines_per_file

        for table_name, dmls in dmls_set.elements.items():
            dmls_write_request = DMLsWriteRequest(
                sink_dml_dir_path=sink_dml_dir_path,
                table_name=table_name,
                dmls=dmls,
                number_of_lines_per_file=number_of_lines_per_file,
            )

            with DMLsWriter(a_request=dmls_write_request) as a_dmls_writer:
                a_dmls_writer.execute()
