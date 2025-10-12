from enum import Enum


class RDBMSType(Enum):
    MY_SQL = ("mysql", 3306)

    @classmethod
    def from_description(cls, key: str):
        for member in cls:
            if member._key == key:
                return member
        raise KeyError(f"'{key}' is not found.")

    def __init__(self, key: str, default_port: int):
        self._key = key
        self._default_port = default_port

    @property
    def key(self) -> str:
        return self._key

    @property
    def default_port(self) -> int:
        return self._default_port
