from dataclasses import dataclass

from shared_code.application.dml.one_table_dmls_writer import (
    OneTableDMLsWriter,
    OneTableDMLsWriteRequest,
)
from shared_code.domain.dmls.list import AllTableDMLs
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath


@dataclass(frozen=True)
class AllTablesDMLsWriteRequest:
    sink_dml_dir_path: SinkDMLDirectoryPath
    all_tables_dmls: AllTableDMLs
    number_of_lines_per_file: NumberOfLinesPerFile


class AllTablesDMLsWriter:
    def __init__(self, a_request: AllTablesDMLsWriteRequest):
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
        all_tables_dmls = a_request.all_tables_dmls
        number_of_lines_per_file = a_request.number_of_lines_per_file

        all_tables_dmls_elements = all_tables_dmls.unmodifiable_elements
        table_count = len(all_tables_dmls_elements)

        for index, one_table_dmls in enumerate(all_tables_dmls.unmodifiable_elements):
            file_name_prefix = str(index + 1).zfill(len(str(table_count)))

            one_table_dmls_write_request = OneTableDMLsWriteRequest(
                sink_dml_dir_path=sink_dml_dir_path,
                file_name_prefix=file_name_prefix,
                one_table_dmls=one_table_dmls,
                number_of_lines_per_file=number_of_lines_per_file,
            )

            with OneTableDMLsWriter(
                a_request=one_table_dmls_write_request
            ) as a_dmls_writer:
                a_dmls_writer.execute()
