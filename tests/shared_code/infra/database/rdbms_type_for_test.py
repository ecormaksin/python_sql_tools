from enum import Enum

from shared_code.infra.database.rdbms_type import RDBMSType


class RDBMSTypeForTest(Enum):
    DB2 = (RDBMSType.DB2, "", "", "")
    MSSQL = (RDBMSType.MSSQL, "", "", "")
    MYSQL = (RDBMSType.MYSQL, "root", "test", """
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
""")
    ORACLE = (RDBMSType.ORACLE, "", "", "")
    POSTGRES = (RDBMSType.POSTGRES, "postgres", "test", "")

    def __init__(self, rdbms_type: RDBMSType, root_username: str, root_password: str, entities_get_query: str):
        self._rdbms_type = rdbms_type
        self._root_username = root_username
        self._root_password = root_password
        self._entities_get_query = entities_get_query

    @property
    def rdbms_type(self) -> RDBMSType:
        return self._rdbms_type

    @property
    def root_username(self) -> str:
        return self._root_username

    @property
    def root_password(self) -> str:
        return self._root_password

    @property
    def entities_get_query(self) -> str:
        return self._entities_get_query
