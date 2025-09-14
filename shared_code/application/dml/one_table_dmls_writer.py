from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generator

from shared_code.domain.dmls.entity import OneTableDmls
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath


@dataclass(frozen=True)
class OneTableDMLsWriteRequest:
    sink_dml_dir_path: SinkDMLDirectoryPath
    file_name_prefix: str
    one_table_dmls: OneTableDmls
    number_of_lines_per_file: NumberOfLinesPerFile


class OneTableDMLsWriter:
    def __init__(self, a_request: OneTableDMLsWriteRequest):
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
        one_table_dmls = a_request.one_table_dmls
        number_of_lines_per_file = a_request.number_of_lines_per_file

        file_count = 0
        if number_of_lines_per_file.file_split_needed():
            chunked_dmls_values = self.__split_dmls()
            file_count, remainder = divmod(
                one_table_dmls.number_of_lines, number_of_lines_per_file.value
            )
            if remainder:
                file_count += 1
        else:
            chunked_dmls_values = [one_table_dmls.dmls]
            file_count = 1

        for index, chunked_dmls_value in enumerate(chunked_dmls_values):
            file_name = self.__get_file_name(index=index, file_count=file_count)
            output_file_path = Path(sink_dml_dir_path.value).joinpath(file_name)

            with open(
                str(output_file_path), "w", newline="", encoding="utf-8"
            ) as file_obj:
                for dml in chunked_dmls_value:
                    file_obj.write(dml + "\n")

    def __split_dmls(self) -> Generator[list[str], Any, None]:
        a_request = self.__a_request
        dmls_elements = a_request.one_table_dmls.dmls
        number_of_lines_per_file = a_request.number_of_lines_per_file
        split_number = number_of_lines_per_file.value

        for i in range(0, len(dmls_elements), split_number):
            yield dmls_elements[i : i + split_number]

    def __get_file_name(self, index: int, file_count: int) -> str:
        a_request = self.__a_request
        file_name_prefix = a_request.file_name_prefix
        table_name = a_request.one_table_dmls.table_name

        file_name = file_name_prefix + "_" + table_name.value
        if file_count > 1:
            file_name += "_" + str(index + 1).zfill(len(str(file_count)))
        file_name += ".sql"

        return file_name
