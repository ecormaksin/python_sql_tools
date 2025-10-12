import datetime
import tempfile
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ulid import ULID

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
from shared_code.infra.file_system.app_config_jsonc_file_reader import (
    AppConfigJsoncFileReader,
)
from shared_code.infra.file_system.directory_creator import DirectoryCreator
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


@dataclass(frozen=True)
class DMLFilesCreationRequest:
    source_data_xlsx_file_path_str: str  # SourceDataXlsxFilePath
    sink_dml_dir_path_str: Optional[str]  # SinkDMLDirectoryPath
    app_config_file_path_str: Optional[str]  # AppConfig


@dataclass(frozen=True)
class DMLFilesCreationResponse:
    sink_dml_dir_path_str: str


class DMLFilesCreator:
    @classmethod
    def execute(cls, a_request: DMLFilesCreationRequest) -> DMLFilesCreationResponse:
        source_data_xlsx_file_path = DMLFilesCreator.__get_source_data_xlsx_file_path(
            file_path_str=a_request.source_data_xlsx_file_path_str
        )

        sink_dml_dir_path = DMLFilesCreator.__get_sink_dml_dir_path(
            dir_path_str=a_request.sink_dml_dir_path_str
        )

        app_config = DMLFilesCreator.__get_app_config(
            file_path_str=a_request.app_config_file_path_str
        )

        all_tables_dmls_build_request = AllTablesDMLsBuildRequest(
            source_data_xlsx_file_path=source_data_xlsx_file_path,
            app_config=app_config,
        )

        all_tables_dmls = AllTablesDMLsBuilder.execute(
            a_request=all_tables_dmls_build_request
        )

        all_tables_dmls_write_request = AllTablesDMLsWriteRequest(
            sink_dml_dir_path=sink_dml_dir_path,
            all_tables_dmls=all_tables_dmls,
            number_of_lines_per_file=app_config.number_of_lines_per_file,
            file_name_prefix=app_config.file_name_prefix,
        )

        AllTablesDMLsWriter.execute(a_request=all_tables_dmls_write_request)

        return DMLFilesCreationResponse(sink_dml_dir_path_str=sink_dml_dir_path.value)

    @classmethod
    def __get_source_data_xlsx_file_path(
        cls, file_path_str: str
    ) -> SourceDataXlsxFilePath:
        if FileExistenceChecker.not_exists(file_path=file_path_str):
            raise RuntimeError(f"Source file '{file_path_str}' not found.")

        return SourceDataXlsxFilePath(value=file_path_str)

    @classmethod
    def __get_sink_dml_dir_path(
        cls, dir_path_str: Optional[str]
    ) -> SinkDMLDirectoryPath:
        sink_dml_dir_path_str = dir_path_str
        if not sink_dml_dir_path_str:
            now = datetime.datetime.now()
            sink_dml_dir_path_str = str(
                Path(tempfile.gettempdir())
                .joinpath("python_sql_tools")
                .joinpath("dml")
                .joinpath(now.strftime("%Y%m%d-%H%M%S") + "-" + str(ULID()))
            )

        try:
            DirectoryCreator.execute(path_str=sink_dml_dir_path_str)
        except IOError | PermissionError:
            stacktrace_str = traceback.format_exc()
            raise RuntimeError(
                f"Cannot create dml output directory '{sink_dml_dir_path_str}'. detail: {stacktrace_str}"
            )

        return SinkDMLDirectoryPath(value=sink_dml_dir_path_str)

    @classmethod
    def __get_app_config(cls, file_path_str: Optional[str]) -> AppConfig:
        config_file_path = file_path_str
        if not config_file_path:
            config_file_path = Path(__file__).parent.parent.parent.parent.joinpath(
                "app_config.json"
            )

        return AppConfigJsoncFileReader.execute(file_path=config_file_path)