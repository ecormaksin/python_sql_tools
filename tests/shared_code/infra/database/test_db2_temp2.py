import pytest
from sqlalchemy import create_engine, text


@pytest.mark.db2
class TestClass:
    def test(self):
        url = "db2+ibm_db://db2inst1:password@localhost:50000/testdb"

        engine = create_engine(url, echo=True)

        with engine.connect() as connection:
            result = connection.execute(text("SELECT TABNAME FROM SYSCAT.TABLES WHERE TABSCHEMA = 'DB2INST1'"))
            print(result.all())
