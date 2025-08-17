from pathlib import Path

import json5

from shared_code.application.app_config.builder import AppConfigBuilder
from shared_code.domain.app_config import AppConfig
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class AppConfigJsoncFileReader:
    def __init__(self, **kwargs):
        if "file_path" in kwargs:
            self.__file_path = kwargs["file_path"]
        else:
            self.__file_path = Path(__file__).parent.parent.parent.parent.joinpath(
                "app_config.json"
            )

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

        with open(file_path, encoding="utf-8") as file_obj:
            config_data = json5.load(file_obj)

        with AppConfigBuilder(config_data=config_data) as config_builder:
            app_config = config_builder.execute()

        return app_config
