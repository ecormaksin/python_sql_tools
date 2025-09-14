from dataclasses import dataclass

from shared_code.application.dml.all_tables_dmls_builder import (
    AllTablesDMLsBuilder,
    AllTablesDMLsBuildRequest,
)
from shared_code.application.dml.all_tables_dmls_writer import (
    AllTablesDMLsWriter,
    AllTablesDMLsWriteRequest,
)
from shared_code.domain.app_config import AppConfig
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath
from shared_code.domain.source_data_xlsx_file_path import SourceDataXlsxFilePath


@dataclass(frozen=True)
class DMLFilesCreationRequest:
    source_data_xlsx_file_path: SourceDataXlsxFilePath
    sink_dml_dir_path: SinkDMLDirectoryPath
    app_config: AppConfig


class DMLFilesCreator:
    def __init__(self, a_request: DMLFilesCreationRequest):
        self.__a_request = a_request

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self):
        a_request = self.__a_request
        app_config = a_request.app_config
        number_of_lines_per_file = app_config.number_of_lines_per_file

        all_tables_dmls_build_request = AllTablesDMLsBuildRequest(
            source_data_xlsx_file_path=a_request.source_data_xlsx_file_path,
            app_config=a_request.app_config,
        )

        all_tables_dmls = AllTablesDMLsBuilder.execute(
            a_request=all_tables_dmls_build_request
        )

        all_tables_dmls_write_request = AllTablesDMLsWriteRequest(
            sink_dml_dir_path=a_request.sink_dml_dir_path,
            all_tables_dmls=all_tables_dmls,
            number_of_lines_per_file=number_of_lines_per_file,
        )

        with AllTablesDMLsWriter(
            a_request=all_tables_dmls_write_request
        ) as all_tables_dmls_writer:
            all_tables_dmls_writer.execute()
