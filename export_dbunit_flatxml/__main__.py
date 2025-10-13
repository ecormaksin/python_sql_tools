from typing import Optional

import click

from shared_code.application.dbunit_flatxml.dbunit_flatxml_exporter import (
    DBUnitFlatXmlExporter,
)


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
    "-T",
    "--tables",
    required=False,
    help="Target table names separated by comma. If not specified, all tables are exported.",
)
@click.option(
    "-d",
    "--destination",
    required=False,
    help="Specify xml's directory path. If not specified, temp directory is used.",
)
def export_dbunit_flatxml(
    db_config: Optional[str],
    tables: Optional[str],
    destination: Optional[str],
):
    """
    This script exports flatxml files for DBUnit.
    """

    xml_dir_path = DBUnitFlatXmlExporter.execute(
        db_config_json_file_path_str=db_config,
        target_tables=tables,
        xml_directory_path_str=destination,
    )

    click.echo(f"xml files were exported at '{xml_dir_path}'.")


if __name__ == "__main__":
    export_dbunit_flatxml()
