from typing import Optional

import click

from shared_code.application.view.view_dependant_table_list_creator import (
    ViewDependantTableListCreator,
)


@click.command()
# @click.option(
#     "-t",
#     "--rdbms-type",
#     required=True,
#     help="RDBMS Type. Currently only 'mysql' is supported.",
# )
@click.option(
    "-T",
    "--view-name",
    required=True,
    help="Specify target view name",
)
@click.option(
    "-C",
    "--db-config",
    required=False,
    help="Database connection configuration json file path. If not specified, project root's 'db_config.json' is used.",
)
@click.option(
    "-d",
    "--destination",
    required=False,
    help="Specify result directory path. If not specified, temp directory is used.",
)
@click.option(
    "-n",
    "--file-name",
    required=False,
    help="Specify result file name. If not specified, 'view_dependant_table_list.txt' is used.",
)
def create_view_dependant_table_list(
        view_name: str,
    db_config: Optional[str], destination: Optional[str], file_name: Optional[str]
):
    """
    This script creates a ddl file.
    """
    result_file_path_str = ViewDependantTableListCreator.execute(
        view_name=view_name,
        db_config_json_file_path_str=db_config,
        list_directory_path_str=destination,
        list_file_name=file_name,
    )

    click.echo(f"result file was created at {result_file_path_str}.")


if __name__ == "__main__":
    create_view_dependant_table_list()
