from sqlalchemy import create_engine, text
from testcontainers.postgres import PostgresContainer

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator import EntityCreator


class TestClass:
    def test(self):
        with PostgresContainer("postgres:18.1") as db_container:
            url = db_container.get_connection_url()
            print(url)  # postgresql+psycopg2://test:test@127.0.0.1:<port>>/test

            engine = create_engine(url, echo=True)

            EntityCreator.execute(engine=engine)

            with engine.connect() as connection:
                result = connection.execute(
                    text(
                        "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'public'"
                    )
                )
                print(result.all())
