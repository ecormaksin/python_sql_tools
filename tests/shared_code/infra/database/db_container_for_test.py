import logging
import re
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists
from testcontainers.mysql import MySqlContainer
from testcontainers.postgres import PostgresContainer

from shared_code.infra.database.rdbms_type import RDBMSType
from shared_code.infra.database.sqlalchemy_sql_file_executor import SQLAlchemySQLFileExecutor
from tests.project_root_resolver import ProjectRootResolver
from tests.shared_code.infra.database.ddl_file_name_control_entity import DDLFileNameControlEntityList
from tests.shared_code.infra.database.rdbms_type_for_test import RDBMSTypeForTest


class DbContainerForTest:
    def __init__(self, rdbms_type: RDBMSType):
        self._rdbms_type = rdbms_type
        rdbms_type_for_test = RDBMSTypeForTest.from_key(key=rdbms_type)
        self._rdbms_type_for_test = rdbms_type_for_test

        logger = logging.getLogger(__name__)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        logger.addHandler(ch)

        project_root = ProjectRootResolver.execute(Path(__file__).resolve())

        common_relative_dirs = ["sample", "docker", rdbms_type.key, "setup"]

        schema_ddl_relative_dirs = list(common_relative_dirs)
        schema_ddl_relative_dirs.append("01.create_databases")
        schema_ddl_dir = project_root.joinpath(*schema_ddl_relative_dirs)

        table_ddl_relative_dirs = list(common_relative_dirs)
        table_ddl_relative_dirs.append("02.create_tables")
        table_ddl_dir = project_root.joinpath(*table_ddl_relative_dirs)

        view_ddl_relative_dirs = list(common_relative_dirs)
        view_ddl_relative_dirs.append("03.create_views")
        view_ddl_dir = project_root.joinpath(*view_ddl_relative_dirs)

        db_container = None

        if rdbms_type == RDBMSType.MYSQL:
            db_container = MySqlContainer(
                image="mysql:9.5.0-oraclelinux9", username=rdbms_type_for_test.root_username,
                root_password=rdbms_type_for_test.root_password
            )

        if rdbms_type == RDBMSType.POSTGRES:
            db_container = PostgresContainer("postgres:18.1", username=rdbms_type_for_test.root_username,
                                             password=rdbms_type_for_test.root_password
                                             )

        if not db_container:
            raise RuntimeError(f"'{rdbms_type.key}' に対応するRDBMSの種類を指定してください。")

        db_container.start()
        self._db_container = db_container

        test_db_url = db_container.get_connection_url()
        logger.info(test_db_url)  # mysql://test:test@localhost:32769/test
        test_db_scheme_replaced_url = rdbms_type.replace_scheme(url=test_db_url)

        for serial_number, ctrl_entity in enumerate(DDLFileNameControlEntityList.get(), start=1):
            schema_name = ctrl_entity.schema_name
            logger.info("")
            logger.info(f"====={schema_name}")

            ddl_file_name = ctrl_entity.get_file_name(serial_number=serial_number)

            url = re.sub("/test$", f"/{schema_name}", test_db_url)
            scheme_replaced_url = rdbms_type.replace_scheme(url=url)

            if not database_exists(scheme_replaced_url):
                original_db_engine = create_engine(test_db_scheme_replaced_url)
                with original_db_engine.connect() as connection:
                    schema_ddl_file = schema_ddl_dir.joinpath(ddl_file_name)
                    SQLAlchemySQLFileExecutor.execute(file_path=schema_ddl_file, connection=connection)

            engine = create_engine(scheme_replaced_url)

            with engine.connect() as connection:
                table_ddl_file = table_ddl_dir.joinpath(ddl_file_name)
                SQLAlchemySQLFileExecutor.execute(file_path=table_ddl_file, connection=connection)

                if ctrl_entity.view:
                    view_ddl_file_name = ctrl_entity.get_view_file_name()
                    view_ddl_file = view_ddl_dir.joinpath(view_ddl_file_name)
                    SQLAlchemySQLFileExecutor.execute(file_path=view_ddl_file, connection=connection)

                query = rdbms_type_for_test.entities_get_query
                result = connection.execute(text(query), {"schema_name": schema_name})
                for row in result:
                    logger.info(f"{row.table_type}: {row.table_name}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        if self._db_container:
            self._db_container.stop()

    @property
    def rdbms_type(self) -> RDBMSType:
        return self._rdbms_type

    @property
    def rdbms_type_for_test(self) -> RDBMSTypeForTest:
        return self._rdbms_type_for_test

    @property
    def db_container(self):
        return self._db_container
