from sqlalchemy import create_engine, text
from testcontainers.mssql import SqlServerContainer
from testcontainers.oracle import OracleDbContainer

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator import EntityCreator


# "container-registry.oracle.com/database/free:23.26.1.0"
class TestClass:
    def test(self):
        with OracleDbContainer() as db_container:
            url = db_container.get_connection_url()
            print(
                url
            )  # oracle+oracledb://system:<password>@localhost:<port>/?service_name=FREEPDB1

            engine = create_engine(url, echo=True)

            EntityCreator.execute(engine=engine)

            with engine.connect() as connection:
                result = connection.execute(text("SELECT TABLE_NAME FROM USER_TABLES"))
                print(result.all())
