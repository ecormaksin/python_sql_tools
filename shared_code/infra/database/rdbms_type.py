from enum import Enum


class RDBMSType(Enum):
    DB2 = ("db2", 50000, "db2", "db2+ibm_db")
    MSSQL = ("mssql", 1433, "mssql", "mssql+pymssql")
    MYSQL = ("mysql", 3306, "mysql", "mysql+pymysql")
    ORACLE = ("oracle", 1521, "oracle", "oracle+oracledb")
    POSTGRES = ("postgres", 5432, "postgresql", "postgresql+psycopg2")

    @classmethod
    def from_key(cls, key: str):
        for member in cls:
            if member._key == key:
                return member
        raise KeyError(f"'{key}' is not found.")

    def __init__(self, key: str, default_port: int, original_scheme: str, replaced_scheme: str):
        self._key = key
        self._default_port = default_port
        self._original_scheme = original_scheme
        self._replaced_scheme = replaced_scheme

    @property
    def key(self) -> str:
        return self._key

    @property
    def default_port(self) -> int:
        return self._default_port

    @property
    def original_scheme(self) -> str:
        return self._original_scheme

    @property
    def replaced_scheme(self) -> str:
        return self._replaced_scheme

    def replace_scheme(self, url: str) -> str:
        return url.replace(f"{self._original_scheme}://", f"{self._replaced_scheme}://")
