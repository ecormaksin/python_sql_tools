from sqlalchemy import create_engine, text
from testcontainers.mssql import SqlServerContainer
from testcontainers.db2 import Db2Container

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator import EntityCreator


class TestClass:
    def test(self):
        with Db2Container(
            "icr.io/db2_community/db2:11.5.9.0"
        ) as db_container:
            url = db_container.get_connection_url()
            print(url)  # db2+ibm_db://db2inst1:password@localhost:<port>/testdb

            engine = create_engine(url, echo=True)

            EntityCreator.execute(engine=engine)

            with engine.connect() as connection:
                result = connection.execute(
                    text("SELECT TABNAME FROM SYSCAT.TABLES")
                )
                print(result.all())

            # db_container.stop(force=True)
