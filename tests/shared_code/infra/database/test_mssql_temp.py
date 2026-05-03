from sqlalchemy import create_engine, text
from testcontainers.mssql import SqlServerContainer


class TestClass:
    def test(self):
        with SqlServerContainer(
                "mcr.microsoft.com/mssql/server:2022-latest"
        ) as db_container:
            url = db_container.get_connection_url()
            print(url)  # mssql+pymssql://SA:1Secure%2APassword1@127.0.0.1:<port>/tempdb

            engine = create_engine(url, echo=True)

            with engine.connect() as connection:
                result = connection.execute(
                    text("SELECT TABLE_NAME FROM information_schema.TABLES")
                )
                print(result.all())
