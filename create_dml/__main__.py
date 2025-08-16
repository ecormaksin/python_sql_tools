import sys
import tempfile

from shared_code.application.dml_creator import DMLCreator


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
        sink_dml_dir_path = tempfile.gettempdir()

    with DMLCreator(
        src_xlsx_file_path=src_xlsx_file_path,
        sink_dml_dir_path=sink_dml_dir_path,
    ) as a_dml_creator:
        a_dml_creator.execute()


if __name__ == "__main__":
    create_dml()
