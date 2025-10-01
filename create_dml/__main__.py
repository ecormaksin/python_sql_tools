import argparse

from rich_argparse import RichHelpFormatter

from shared_code.application.dml.dml_files_creator import (
    DMLFilesCreationRequest,
    DMLFilesCreator,
)


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

    a_request = DMLFilesCreationRequest(
        source_data_xlsx_file_path_str=args.source,
        sink_dml_dir_path_str=args.destination,
        app_config_file_path_str=args.config,
    )

    a_response = DMLFilesCreator.execute(a_request=a_request)

    sink_dml_dir_path_str = a_response.sink_dml_dir_path_str
    print(f"DML files are created at '{sink_dml_dir_path_str}'.")


if __name__ == "__main__":
    create_dml()
