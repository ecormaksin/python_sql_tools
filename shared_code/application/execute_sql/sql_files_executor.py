import datetime
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import mysql.connector
from ulid import ULID

from shared_code.infra.database.rdbms_type import RDBMSType
from shared_code.infra.file_system.directory_creator import DirectoryCreator
from shared_code.infra.file_system.file_writer import FileWriter

SQL_STATEMENT_DEFAULT_DELIMITER = ";"


@dataclass(frozen=True)
class SQLFilesExecuteRequest:
    source_sql_files_directory_path_str: str
    rdbms_type_str: str
    host: str
    user: str
    password: str
    port: Optional[int]
    database: str
    delimiter: Optional[str]
    log_directory_path_str: Optional[str]


class SQLFilesExecutor:
    @classmethod
    def execute(
        cls,
        source: str,
        host: str,
        user: str,
        password: str,
        port: Optional[int],
        database: str,
        delimiter: Optional[str],
        log: Optional[str],
    ):
        rdbms_type = RDBMSType.MY_SQL

        log_dir_path_str = cls.__get_log_dir_path_str(log_dir_path_str=log)
        DirectoryCreator.execute(path_str=log_dir_path_str)

        a_request = SQLFilesExecuteRequest(
            source_sql_files_directory_path_str=source,
            rdbms_type_str=rdbms_type.key,
            host=host,
            user=user,
            password=password,
            port=port if port else rdbms_type.default_port,
            database=database,
            delimiter=delimiter if delimiter else SQL_STATEMENT_DEFAULT_DELIMITER,
            log_directory_path_str=log_dir_path_str,
        )

        src_dir_path = a_request.source_sql_files_directory_path_str

        sql_file_paths = Path(src_dir_path).rglob("*.sql")

        for sql_file_path in sql_file_paths:
            cls.__execute_sql_file(
                a_request=a_request, sql_file_path_str=str(sql_file_path)
            )

        return log_dir_path_str

    @classmethod
    def __get_log_dir_path_str(cls, log_dir_path_str: Optional[str]) -> str:
        dir_path_str = log_dir_path_str
        if not dir_path_str:
            now = datetime.datetime.now()
            dir_path_str = str(
                Path(tempfile.gettempdir())
                .joinpath("python_sql_tools")
                .joinpath("execute_sql")
                .joinpath(now.strftime("%Y%m%d-%H%M%S") + "-" + str(ULID()))
            )
        return dir_path_str

    @classmethod
    def __execute_sql_file(
        cls, a_request: SQLFilesExecuteRequest, sql_file_path_str: str
    ):
        sql_file_path = Path(sql_file_path_str)
        sql_file_name = sql_file_path.stem
        log_file_path_str = str(
            Path(a_request.log_directory_path_str).joinpath(sql_file_name + ".log")
        )

        FileWriter.tee_append(
            file_path_str=log_file_path_str,
            content=f"'{sql_file_path_str}' execution start.",
        )

        with open(sql_file_path_str, "r", encoding="utf-8") as file_obj:
            content = file_obj.read()

        delimiter = a_request.delimiter

        if delimiter == SQL_STATEMENT_DEFAULT_DELIMITER:
            statements = content.splitlines()
        else:
            statements = content.split(delimiter)

        cls.__execute_sql_statements(
            a_request=a_request,
            statements=statements,
            log_file_path_str=log_file_path_str,
        )

        FileWriter.tee_append(
            file_path_str=log_file_path_str,
            content=f"'{sql_file_path_str}' execution finished.",
        )

    @classmethod
    def __execute_sql_statements(
        cls,
        a_request: SQLFilesExecuteRequest,
        statements: list[str],
        log_file_path_str: str,
    ):
        config = {
            "host": a_request.host,
            "user": a_request.user,
            "password": a_request.password,
            "port": a_request.port,
            "database": a_request.database,
        }

        with mysql.connector.connect(**config) as cnx:
            with cnx.cursor() as cur:
                for statement in statements:
                    if not statement.strip():
                        continue

                    operation = statement

                    FileWriter.tee_append(
                        file_path_str=log_file_path_str,
                        content="start: " + operation,
                    )

                    cur.execute(operation)
                    cnx.commit()

                    FileWriter.tee_append(
                        file_path_str=log_file_path_str,
                        content="finished: " + operation,
                    )
