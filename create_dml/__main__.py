import argparse
import datetime
import sys
import tempfile
import traceback
from pathlib import Path

from rich_argparse import RichHelpFormatter

from shared_code.application.dml.dml_files_creator import (
    DMLFilesCreationRequest,
    DMLFilesCreator,
)
from shared_code.domain.sink_dml_dir_path import SinkDMLDirectoryPath
from shared_code.domain.source_data_xlsx_file_path import SourceDataXlsxFilePath
from shared_code.infra.file_system.app_config_jsonc_file_reader import (
    AppConfigJsoncFileReader,
)
from shared_code.infra.file_system.directory_creator import DirectoryCreator
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


def create_dml():
    arg_parser = argparse.ArgumentParser(
        description="This script creates dml files from .xlsx file.",
        formatter_class=RichHelpFormatter,
    )
    arg_parser.add_argument(
        "-s", "--source", help="Specify source .xlsx file path.", required=True
    )
    arg_parser.add_argument(
        "-d",
        "--destination",
        help="Specify dml's directory path. If not specified, temp directory is used.",
    )
    arg_parser.add_argument(
        "-c",
        "--config",
        help="Specify a configuration json file path. If not specified, project root's 'app_config.json' is used.",
    )

    args = arg_parser.parse_args()

    src_xlsx_file_path_str = args.source
    if args.destination:
        sink_dml_dir_path_str = args.destination
    else:
        now = datetime.datetime.now()
        sink_dml_dir_path_str = str(
            Path(tempfile.gettempdir())
            .joinpath("python-sql-tools")
            .joinpath("dml")
            .joinpath(now.strftime("%Y%m%d-%H%M%S"))
        )

    if args.config:
        config_file_path = args.config
    else:
        config_file_path = Path(__file__).parent.parent.joinpath("app_config.json")

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

    app_config = AppConfigJsoncFileReader.execute(file_path=config_file_path)

    a_request = DMLFilesCreationRequest(
        source_data_xlsx_file_path=SourceDataXlsxFilePath(value=src_xlsx_file_path_str),
        sink_dml_dir_path=SinkDMLDirectoryPath(value=sink_dml_dir_path_str),
        app_config=app_config,
    )

    DMLFilesCreator.execute(a_request=a_request)

    print(f"DML files are created at '{sink_dml_dir_path_str}'.")


if __name__ == "__main__":
    create_dml()
