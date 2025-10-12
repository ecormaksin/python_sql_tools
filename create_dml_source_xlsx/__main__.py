from typing import Optional

import click

from shared_code.application.dml_source_xlsx.dml_source_xlsx_creator import (
    DMLSourceXlsxCreator,
)


@click.command()
# @click.option(
#     "-t",
#     "--rdbms-type",
#     required=True,
#     help="RDBMS Type. Currently only 'mysql' is supported.",
# )
@click.option(
    "-c",
    "--app-config",
    help="Specify a configuration json file path. If not specified, project root's 'app_config.json' is used.",
)
@click.option(
    "-C",
    "--db-config",
    required=False,
    help="Database connection configuration json file path. If not specified, project root's 'db_config.json' is used.",
)
@click.option(
    "-T",
    "--tables",
    required=False,
    help="Target table names separated by comma. If not specified, all tables are created.",
)
@click.option(
    "-d",
    "--destination",
    required=False,
    help="Specify xlsx's directory path. If not specified, temp directory is used.",
)
@click.option(
    "-n",
    "--file-name",
    required=False,
    help="Specify xlsx's file name. If not specified, 'dml_source.xlsx' is used.",
)
def create_source_xlsx(
    app_config: Optional[str],
    db_config: Optional[str],
    tables: Optional[str],
    destination: Optional[str],
    file_name: Optional[str],
):
    """
    This script creates dml source xlsx file.
    """

    xlsx_file_path = DMLSourceXlsxCreator.execute(
        app_config_json_file_path_str=app_config,
        db_config_json_file_path_str=db_config,
        target_tables=tables,
        xlsx_directory_path_str=destination,
        dml_source_file_name=file_name,
    )

    click.echo(f"xlsx file was created at '{xlsx_file_path}'.")


if __name__ == "__main__":
    create_source_xlsx()
