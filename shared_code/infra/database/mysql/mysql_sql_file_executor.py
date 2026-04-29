from pathlib import Path

from shared_code.infra.database.sql_splitter import SQLSplitter


class MySQLFileExecutor:
    @classmethod
    def execute(cls, file_path: Path, db_cursor, separator: str = ";"):
        with open(file_path) as f:
            file_content = f.read()

        ddl_list = SQLSplitter.execute(source=file_content, separator=separator)
        for ddl in ddl_list:
            db_cursor.execute(ddl)
