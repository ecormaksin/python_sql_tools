from shared_code.application.app_config.builder import AppConfigBuilder
from shared_code.application.db_column.list_builder import (
    DBColumnsBuildRequest,
    DBColumnsBuilder,
)
from shared_code.domain.db_column.list import DBColumns
from tests.shared_code.application.db_column.list_test_data import DBColumnsTestData
from tests.shared_code.domain.app_config_for_test import AppConfigForTest


class DBColumnsTestBuilder:
    @staticmethod
    def media_type() -> DBColumns:
        source_data = DBColumnsTestData.MEDIA_TYPE

        config_data = AppConfigForTest.get_config_data(
            data_str=AppConfigForTest.TABLE_NAME_SHEET_VALID_SAMPLE_DATA_STR
        )
        with AppConfigBuilder(config_data=config_data) as app_config_builder:
            app_config = app_config_builder.execute()

        a_request = DBColumnsBuildRequest(
            source_data=source_data, app_config=app_config
        )
        return DBColumnsBuilder.execute(a_request=a_request)
