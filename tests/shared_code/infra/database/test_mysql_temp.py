import re

from sqlalchemy import create_engine, text
from sqlalchemy_utils import create_database, database_exists
from testcontainers.mysql import MySqlContainer

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator_map import (
    EntityCreatorMap,
)


class TestClass:
    def test(self):
        with MySqlContainer(
            image="mysql:9.5.0-oraclelinux9", username="root", root_password="test"
        ) as db_container:
            original_url = db_container.get_connection_url()

            entity_creator_map = EntityCreatorMap.get()

            for db_name, entity_creator in entity_creator_map.items():
                print(f"====={db_name}")
                url = re.sub("/test$", f"/{db_name}", original_url)
                print(url)  # mysql://test:test@localhost:32769/test

                url = url.replace("mysql://", "mysql+pymysql://")

                if not database_exists(url):
                    create_database(url)

                engine = create_engine(url, echo=True)

                entity_creator.execute(engine=engine)

                with engine.connect() as connection:
                    result = connection.execute(
                        text(
                            f"SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = '{db_name}'"
                        )
                    )
                    print(result.all())
