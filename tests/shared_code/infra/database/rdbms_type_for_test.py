from enum import Enum

from sqlalchemy import text
from sqlalchemy.engine.base import Connection
from sqlalchemy_utils import database_exists
from testcontainers.core.generic import DbContainer
from testcontainers.mysql import MySqlContainer
from testcontainers.postgres import PostgresContainer

from shared_code.infra.database.rdbms_type import RDBMSType


def check_database_exists_by_url_only(
    url: str, connection: Connection, schema_name: str
) -> bool:
    return database_exists(url)


def check_database_exists_for_postgres(
    url: str, connection: Connection, schema_name: str
) -> bool:
    query = """
    select 
        schema_name
    from
        information_schema.schemata
    where 
        schema_name = :schema_name
    """

    result = connection.execute(text(query), {"schema_name": schema_name}).fetchall()

    return len(result) > 0


class RDBMSTypeForTest(Enum):
    # DB2 = (RDBMSType.DB2, "", "", "")
    # MSSQL = (RDBMSType.MSSQL, "", "", "")
    # ORACLE = (RDBMSType.ORACLE, "", "", "")
    MYSQL = (
        RDBMSType.MYSQL,
        MySqlContainer(
            image="mysql:9.5.0-oraclelinux9",
            username="root",
            root_password="test",
            password="test",
        ),
        check_database_exists_by_url_only,
        """
SELECT 
    case 
        when TABLE_TYPE = 'BASE TABLE' then 'table'
        when TABLE_TYPE = 'VIEW' then 'view'
        else 'system_view(INFORMATION_SCHEMA)'
    end as table_type,
    TABLE_NAME as table_name
FROM 
    information_schema.TABLES
where 
    TABLE_SCHEMA = :schema_name
order by 
    case 
        when TABLE_TYPE = 'BASE TABLE' then 1
        when TABLE_TYPE = 'VIEW' then 2
        else 3
    end,
    TABLE_NAME    
""",
    )
    POSTGRES = (
        RDBMSType.POSTGRES,
        PostgresContainer(
            "postgres:18.1",
            username="postgres",
            password="test",
        ),
        check_database_exists_for_postgres,
        """
SELECT 
    case 
        when TABLE_TYPE = 'BASE TABLE' then 'table'
        when TABLE_TYPE = 'VIEW' then 'view'
        WHEN table_type = 'FOREIGN' THEN 'foreign'
        WHEN table_type = 'LOCAL TEMPORARY' THEN 'local_temporary'
        ELSE 'unknown'
    end as table_type,
    TABLE_NAME as table_name
FROM 
    information_schema.tables 
where 
    TABLE_SCHEMA = :schema_name
order by 
    case 
        when TABLE_TYPE = 'BASE TABLE' then 1
        when TABLE_TYPE = 'VIEW' then 2
        else 3
    end,
    TABLE_NAME    
""",
    )

    def __init__(
        self,
        rdbms_type: RDBMSType,
        db_container: DbContainer,
        check_database_exists_func,
        entities_get_query: str,
    ):
        self._rdbms_type = rdbms_type
        self._db_container = db_container
        self._check_database_exists_func = check_database_exists_func
        self._entities_get_query = entities_get_query

    @classmethod
    def from_key(cls, key: RDBMSType):
        for member in cls:
            if member._rdbms_type == key:
                return member
        raise KeyError(f"'{key.key}' is not found.")

    @property
    def rdbms_type(self) -> RDBMSType:
        return self._rdbms_type

    @property
    def db_container(self) -> DbContainer:
        return self._db_container

    @property
    def entities_get_query(self) -> str:
        return self._entities_get_query

    def check_database_exists(
        self, url: str, connection: Connection, schema_name: str
    ) -> bool:
        return self._check_database_exists_func(url, connection, schema_name)
