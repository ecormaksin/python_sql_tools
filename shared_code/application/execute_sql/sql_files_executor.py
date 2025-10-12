from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from shared_code.application.app_directory_creator import AppDirectoryCreator
from shared_code.application.app_file_utils import AppFileUtils
from shared_code.infra.database.mysql.connector import MySQLConnector
from shared_code.infra.file_system.file_writer import FileWriter

SQL_STATEMENT_DEFAULT_DELIMITER = ";"


@dataclass(frozen=True)
class SQLFilesExecuteRequest:
    delimiter: Optional[str]
    log_directory_path_str: Optional[str]


@dataclass(frozen=True)
class DatabaseOperationObjects:
    db_connection: Any
    cursor: Any


class SQLFilesExecutor:
    @classmethod
    def execute(
        cls,
        source_sql_files_directory_path_str: str,
        db_config_json_file_path_str: Optional[str],
        delimiter: Optional[str],
        log_directory_path_str: Optional[str],
    ):
        db_config_file_path_str = AppFileUtils.determine_and_check(
            arg_file_path_str=db_config_json_file_path_str,
            default_file_path=Path(__file__).parent.parent.parent.parent.joinpath(
                "db_config.json"
            ),
        )

        log_dir_path_str = AppDirectoryCreator.execute(
            module_name="execute_sql",
            directory_type="log",
            directory_path_str=log_directory_path_str,
        )

        a_request = SQLFilesExecuteRequest(
            delimiter=delimiter if delimiter else SQL_STATEMENT_DEFAULT_DELIMITER,
            log_directory_path_str=log_dir_path_str,
        )

        sql_file_paths = Path(source_sql_files_directory_path_str).rglob("*.sql")

        with MySQLConnector(
            config_json_file_path_str=db_config_file_path_str
        ) as db_connector:
            db_connection = db_connector.connect()
            with db_connection.cursor() as cursor:
                db_op_obj = DatabaseOperationObjects(
                    db_connection=db_connection, cursor=cursor
                )

                for sql_file_path in sql_file_paths:
                    cls.__execute_sql_file(
                        db_op_obj=db_op_obj,
                        a_request=a_request,
                        sql_file_path_str=str(sql_file_path),
                    )

        return log_dir_path_str

    @classmethod
    def __execute_sql_file(
        cls,
        db_op_obj: DatabaseOperationObjects,
        a_request: SQLFilesExecuteRequest,
        sql_file_path_str: str,
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
            db_op_obj=db_op_obj,
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
        db_op_obj: DatabaseOperationObjects,
        statements: list[str],
        log_file_path_str: str,
    ):
        for statement in statements:
            if not statement.strip():
                continue

            operation = statement

            FileWriter.tee_append(
                file_path_str=log_file_path_str,
                content="start: " + operation,
            )

            db_op_obj.cursor.execute(operation)
            db_op_obj.db_connection.commit()

            FileWriter.tee_append(
                file_path_str=log_file_path_str,
                content="finished: " + operation,
            )
