from dataclasses import dataclass


from shared_code.application.dml.dmls_set_builder import (
    DMLsSetBuildRequest,
    DMLsSetBuilder,
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

        dmls_set_build_request = DMLsSetBuildRequest(
            source_data_xlsx_file_path=a_request.source_data_xlsx_file_path,
            app_config=a_request.app_config,
        )

        with DMLsSetBuilder(a_request=dmls_set_build_request) as a_dmls_set_builder:
            dmls_set = a_dmls_set_builder.execute()
