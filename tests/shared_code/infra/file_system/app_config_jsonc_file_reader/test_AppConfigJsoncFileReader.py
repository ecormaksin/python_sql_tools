from pathlib import Path

from shared_code.infra.file_system.app_config_jsonc_file_reader import (
    AppConfigJsoncFileReader,
)


class TestClass:
    def test_default_config_read(self):
        file_path = (
            Path(__file__).parent.joinpath("test_data").joinpath("app_config.json")
        )
        app_config = AppConfigJsoncFileReader.execute(file_path=str(file_path))

        assert app_config