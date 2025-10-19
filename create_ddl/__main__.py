from typing import Optional

import click

from shared_code.application.ddl.ddl_file_creator import DDLFileCreator


@click.command()
# @click.option(
#     "-t",
#     "--rdbms-type",
#     required=True,
#     help="RDBMS Type. Currently only 'mysql' is supported.",
# )
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
    help="Specify ddl's directory path. If not specified, temp directory is used.",
)
@click.option(
    "-n",
    "--file-name",
    required=False,
    help="Specify ddl's file name. If not specified, 'ddl.sql' is used.",
)
def create_ddl(
    db_config: Optional[str], destination: Optional[str], file_name: Optional[str]
):
    """
    This script creates a ddl file.
    """
    ddl_file_path_str = DDLFileCreator.execute(
        db_config_json_file_path_str=db_config,
        ddl_directory_path_str=destination,
        ddl_file_name=file_name,
    )

    click.echo(f"ddl file was exported at {ddl_file_path_str}.")


if __name__ == "__main__":
    create_ddl()
