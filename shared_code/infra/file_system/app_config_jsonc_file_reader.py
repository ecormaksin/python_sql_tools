from pathlib import Path

from shared_code.domain.app_config import AppConfig
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class AppConfigJsoncFileReader:
    def __init__(self, **kwargs):
        if "file_path" in kwargs:
            self.__file_path = kwargs["file_path"]
        else:
            self.__file_path = Path(__file__).parent.parent.parent.parent.joinpath("app_config.json")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> AppConfig:
        file_path = self.__file_path

        if FileExistenceChecker.not_exists(file_path=file_path):
            raise RuntimeError(f"config file '{file_path}' not found.")
