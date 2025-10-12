from typing import Optional

import click

from shared_code.application.dml.dml_files_creator import (
    DMLFilesCreationRequest,
    DMLFilesCreator,
)


@click.command()
@click.option("-s", "--source", help="Specify source .xlsx file path.", required=True)
@click.option(
    "-d",
    "--destination",
    help="Specify dml's directory path. If not specified, temp directory is used.",
)
@click.option(
    "-c",
    "--config",
    help="Specify a configuration json file path. If not specified, project root's 'app_config.json' is used.",
)
def create_dml(source: str, destination: Optional[str], config: Optional[str]):
    """
    This script creates dml files from .xlsx file.
    """

    a_request = DMLFilesCreationRequest(
        source_data_xlsx_file_path_str=source,
        sink_dml_dir_path_str=destination,
        app_config_file_path_str=config,
    )

    a_response = DMLFilesCreator.execute(a_request=a_request)

    sink_dml_dir_path_str = a_response.sink_dml_dir_path_str
    click.echo(f"DML files are created at '{sink_dml_dir_path_str}'.")


if __name__ == "__main__":
    create_dml()
