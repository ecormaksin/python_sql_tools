from shared_code.application.app_config.builder import AppConfigBuilder
from shared_code.application.db_column.entity_builder import (
    DBColumnBuilder,
    DBColumnBuildRequest,
)
from tests.shared_code.domain.app_config_for_test import AppConfigForTest


class TestClass:
    def test_entity_with_key_position(self):
        source_data = ["media_type_id", "media_type_id", "INT", "1", "None"]

        config_data = AppConfigForTest.get_config_data(
            data_str=AppConfigForTest.TABLE_NAME_SHEET_VALID_SAMPLE_DATA_STR
        )
        with AppConfigBuilder(config_data=config_data) as app_config_builder:
            app_config = app_config_builder.execute()

        a_request = DBColumnBuildRequest(source_data=source_data, app_config=app_config)
        db_column = DBColumnBuilder.execute(a_request=a_request)

        assert db_column
        assert db_column.column_name.value == "media_type_id"
        assert db_column.data_type.value == "INT"
        assert db_column.key_position.value == "1"
        assert db_column.no_quotation is None
