from pathlib import Path

from sqlalchemy import text
from sqlalchemy.engine.base import Connection

from shared_code.infra.database.sql_splitter import SQLSplitter


class SQLAlchemySQLFileExecutor:
    @classmethod
    def execute(cls, file_path: Path, connection: Connection, separator: str = ";"):
        with open(file_path) as f:
            file_content = f.read()

        ddl_list = SQLSplitter.execute(source=file_content, separator=separator)
        for ddl in ddl_list:
            connection.execute(text(ddl))
