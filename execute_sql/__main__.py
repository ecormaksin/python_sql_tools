from typing import Optional

import click

from shared_code.application.execute_sql.sql_files_executor import SQLFilesExecutor


@click.command()
@click.option(
    "-s",
    "--source",
    required=True,
    help="Source .sql directory path.(processed recursively)",
)
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
    "--delimiter",
    required=False,
    help="The statement delimiter.(default ';')",
)
@click.option(
    "-l",
    "--log",
    required=False,
    help="Log directory(default tempdir)",
)
def execute_sql(
    source: str,
    db_config: Optional[str],
    delimiter: Optional[str],
    log: Optional[str],
):
    """
    This script recursively executes SQL files stored in the specified directory.
    """
    log_dir_path_str = SQLFilesExecutor.execute(
        source_sql_files_directory_path_str=source,
        db_config_json_file_path_str=db_config,
        delimiter=delimiter,
        log_directory_path_str=log,
    )

    click.echo(f"Log files were created at '{log_dir_path_str}'.")


if __name__ == "__main__":
    execute_sql()
