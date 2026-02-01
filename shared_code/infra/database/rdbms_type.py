from enum import Enum


class RDBMSType(Enum):
    DB2 = ("db2", 50000, "db2+ibm_db")
    MSSQL = ("mssql", 1433, "mssql+pymssql")
    MYSQL = ("mysql", 3306, "mysql+pymysql")
    ORACLE = ("oracle", 1521, "oracle+oracledb")
    POSTGRES  = ("postgres", 5432, "postgresql+psycopg2")

    @classmethod
    def from_key(cls, key: str):
        for member in cls:
            if member._key == key:
                return member
        raise KeyError(f"'{key}' is not found.")

    def __init__(self, key: str, default_port: int, driver_name: str):
        self._key = key
        self._default_port = default_port
        self._driver_name = driver_name

    @property
    def key(self) -> str:
        return self._key

    @property
    def default_port(self) -> int:
        return self._default_port

    @property
    def driver_name(self) -> str:
        return self._driver_name
