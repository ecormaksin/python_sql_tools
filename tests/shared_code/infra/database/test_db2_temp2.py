import pytest
from sqlalchemy import create_engine, text

from tests.shared_code.infra.database.sqlalchemy.orm.entity_creator import EntityCreator


@pytest.mark.db2
class TestClass:
    def test(self):
        url = "db2+ibm_db://db2inst1:password@localhost:50000/testdb"

        engine = create_engine(url, echo=True)

        EntityCreator.execute(engine=engine)

        with engine.connect() as connection:
            result = connection.execute(text("SELECT TABNAME FROM SYSCAT.TABLES"))
            print(result.all())
