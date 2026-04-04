from sqlalchemy import create_engine, text
from testcontainers.mysql import MySqlContainer

from sqlalchemy_utils import database_exists, create_database
import re

from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist_db_entity_creator import ArtistDbEntityCreator


class TestClass:
    def test(self):
        with MySqlContainer(image="mysql:9.5.0-oraclelinux9", username='root', root_password='test') as db_container:
            original_url = db_container.get_connection_url()
            
            url = re.sub("/test$", "/artist", original_url)
            print(url) # mysql://test:test@localhost:32769/test

            url = url.replace("mysql://", "mysql+pymysql://")

            if not database_exists(url):
                create_database(url)

            engine = create_engine(url, echo=True)

            ArtistDbEntityCreator.execute(engine=engine)

            with engine.connect() as connection:
                result = connection.execute(
                    text(
                        "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'artist'"
                    )
                )
                print(result.all())
