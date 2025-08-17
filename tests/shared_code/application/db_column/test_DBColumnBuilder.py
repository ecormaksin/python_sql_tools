import json

from shared_code.application.app_config.builder import AppConfigBuilder
from shared_code.application.db_column.entity_builder import (
    DBColumnBuilder,
    DBColumnBuildRequest,
)


class TestClass:
    def test_entity_creation(self):
        source_data = ["media_type_id", "media_type_id", "INT", "1", "None"]
        config_data_str = """
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "key_position_row": 4,
  "no_quotation_row": 5,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 1000
}
"""

        config_data = json.loads(config_data_str)
        with AppConfigBuilder(config_data=config_data) as app_config_builder:
            app_config = app_config_builder.execute()

        a_request = DBColumnBuildRequest(source_data=source_data, app_config=app_config)
        db_column = DBColumnBuilder.execute(a_request=a_request)

        assert db_column
