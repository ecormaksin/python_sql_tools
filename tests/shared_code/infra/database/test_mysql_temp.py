from sqlalchemy import create_engine, text
from testcontainers.mysql import MySqlContainer

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator import EntityCreator


class TestClass:
    def test(self):
        with MySqlContainer("mysql:9.5.0-oraclelinux9") as db_container:
            url = db_container.get_connection_url()
            print(url)

            url = url.replace("mysql://", "mysql+pymysql://")

            engine = create_engine(url, echo=True)

            EntityCreator.execute(engine=engine)

            with engine.connect() as connection:
                result = connection.execute(
                    text(
                        "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'test'"
                    )
                )
                print(result.all())
