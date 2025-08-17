from openpyxl.worksheet.worksheet import Worksheet

from shared_code.domain.app_config import AppConfig
from shared_code.domain.table_name import TableName


class DMLCreator:
    def __init__(
        self, table_name: TableName, a_worksheet: Worksheet, app_config: AppConfig
    ):
        self.__table_name = table_name
        self.__a_worksheet = a_worksheet
        self.__app_config = app_config

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> list[str]:
        table_name = self.__table_name
        a_worksheet = self.__a_worksheet
        app_config = self.__app_config
        return []
