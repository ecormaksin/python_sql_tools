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
    "-h",
    "--host",
    required=True,
    help="Host on which database server is located.",
)
@click.option(
    "-u",
    "--user",
    required=True,
    help="User name to use when connecting to server.",
)
@click.option(
    "-p",
    "--password",
    required=True,
    help="Password to use when connecting to server.",
)
@click.option(
    "-D",
    "--database",
    required=True,
    help="The database to use.",
)
@click.option(
    "-P",
    "--port",
    required=False,
    help="TCP/IP port number for connection.",
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
    host: str,
    user: str,
    password: str,
    port: Optional[int],
    database: str,
    delimiter: Optional[str],
    log: Optional[str],
):
    """
    This script recursively executes SQL files stored in the specified directory.
    """
    log_dir_path_str = SQLFilesExecutor.execute(
        source=source,
        host=host,
        user=user,
        password=password,
        port=port,
        database=database,
        delimiter=delimiter,
        log=log,
    )

    click.echo(f"Log files were created at '{log_dir_path_str}'.")


if __name__ == "__main__":
    execute_sql()
