import sys
import tempfile
from pathlib import Path

from ulid import ULID

from shared_code.application.dml_files_creator import DMLFilesCreator
from shared_code.infra.file_system.app_config_jsonc_file_reader import (
    AppConfigJsoncFileReader,
)


def create_dml():
    args_len = len(sys.argv)
    if args_len < 2:
        print(
            "Usage: <source_data_xlsx_file_path> (<dml_output_directory_path> if not specified, temp directory is used.)"
        )
        sys.exit(1)

    src_xlsx_file_path = sys.argv[1]
    if args_len >= 3:
        sink_dml_dir_path = sys.argv[2]
    else:
        sink_dml_dir_path = str(Path(tempfile.gettempdir()).joinpath(str(ULID())))

    with AppConfigJsoncFileReader() as config_reader:
        app_config = config_reader.execute()

    with DMLFilesCreator(
        src_xlsx_file_path=src_xlsx_file_path,
        sink_dml_dir_path=sink_dml_dir_path,
        app_config=app_config,
    ) as a_dml_creator:
        a_dml_creator.execute()


if __name__ == "__main__":
    create_dml()
