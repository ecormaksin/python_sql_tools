import json5

from shared_code.application.app_config.builder.entity import AppConfigBuilder
from shared_code.domain.app_config import AppConfig
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class AppConfigJsoncFileReader:
    @classmethod
    def execute(cls, file_path: str) -> AppConfig:
        if FileExistenceChecker.not_exists(file_path=file_path):
            raise RuntimeError(f"config file '{file_path}' not found.")

        with open(file_path, encoding="utf-8") as file_obj:
            config_data = json5.load(file_obj)

        with AppConfigBuilder(config_data=config_data) as config_builder:
            app_config = config_builder.execute()

        return app_config
