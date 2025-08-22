import sys
import tempfile
import traceback
from pathlib import Path

from ulid import ULID

from shared_code.application.dml.dml_files_creator import (
    DMLFilesCreator,
    DMLFilesCreationRequest,
)
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath
from shared_code.domain.source_data_xlsx_file_path import SourceDataXlsxFilePath
from shared_code.infra.file_system.app_config_jsonc_file_reader import (
    AppConfigJsoncFileReader,
)
from shared_code.infra.file_system.directory_creator import DirectoryCreator
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


def create_dml():
    args_len = len(sys.argv)
    if args_len < 2:
        print(
            "Usage: <source_data_xlsx_file_path> (<dml_output_directory_path> if not specified, temp directory is used.)"
        )
        sys.exit(1)

    src_xlsx_file_path_str = sys.argv[1]
    if args_len >= 3:
        sink_dml_dir_path_str = sys.argv[2]
    else:
        sink_dml_dir_path_str = str(Path(tempfile.gettempdir()).joinpath(str(ULID())))

    if FileExistenceChecker.not_exists(file_path=src_xlsx_file_path_str):
        print(f"Source file '{src_xlsx_file_path_str}' not found.")
        sys.exit(1)

    try:
        DirectoryCreator.execute(path_str=sink_dml_dir_path_str)
    except IOError | PermissionError:
        stacktrace_str = traceback.format_exc()
        print(
            f"Cannot create dml output directory '{sink_dml_dir_path_str}'. detail: {stacktrace_str}"
        )
        sys.exit(1)

    with AppConfigJsoncFileReader() as config_reader:
        app_config = config_reader.execute()

    a_request = DMLFilesCreationRequest(
        source_data_xlsx_file_path=SourceDataXlsxFilePath(value=src_xlsx_file_path_str),
        sink_dml_dir_path=SinkDMLDirectoryPath(value=sink_dml_dir_path_str),
        app_config=app_config,
    )

    with DMLFilesCreator(
        a_request=a_request,
    ) as a_dml_creator:
        a_dml_creator.execute()

    print(f"DML files are created at '{sink_dml_dir_path_str}'.")


if __name__ == "__main__":
    create_dml()
