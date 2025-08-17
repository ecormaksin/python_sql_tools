from shared_code.application.app_config.builder import AppConfigBuilder
from shared_code.application.db_column.list_builder import (
    DBColumnsBuildRequest,
    DBColumnsBuilder,
)
from tests.shared_code.domain.app_config_for_test import AppConfigForTest


class TestClass:
    def test_list_build(self):
        source_data = [
            ["media_type_id", "media_type_id", "INT", "1", "None"],
            ["name", "name", "VARCHAR(10)", "None", "None"],
        ]

        config_data = AppConfigForTest.get_config_data(
            data_str=AppConfigForTest.TABLE_NAME_SHEET_VALID_SAMPLE_DATA_STR
        )
        with AppConfigBuilder(config_data=config_data) as app_config_builder:
            app_config = app_config_builder.execute()

        a_request = DBColumnsBuildRequest(
            source_data=source_data, app_config=app_config
        )
        db_columns = DBColumnsBuilder.execute(a_request=a_request)

        assert db_columns
        assert len(db_columns.unmodifiable_elements) == 2
