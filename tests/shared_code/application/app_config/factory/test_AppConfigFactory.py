import json
from dataclasses import dataclass
from typing import Optional, Type

import pytest

from shared_code.application.app_config.factory import AppConfigFactory

test_params = list(enumerate(["no properties", "'table_name' missing", "'table_name_cell' missing", "'table_name's value not defined", "'column_name_row' invalid"]))

@dataclass(frozen=True)
class Item:
    config_data_str: str
    expected_exception: Optional[Type[Exception]]

test_values = [
    Item(config_data_str="{}", expected_exception=RuntimeError),
    Item(
        config_data_str="""
{
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 2
  }
}
""",
        expected_exception=RuntimeError,
    ),
    Item(
        config_data_str="""
{
  "table_name": "cell",
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 2
  }
}
""",
        expected_exception=RuntimeError,
    ),
    Item(
        config_data_str="""
{
  "table_name": "row",
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 2
  }
}
""",
        expected_exception=RuntimeError,
    ),
    Item(
        config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 0,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 2
  }
}
""",
        expected_exception=RuntimeError,
    ),
]

class TestClass:
    @pytest.mark.parametrize("no, description", [(index+1, description) for index, (description) in test_params])
    def test_pattern(self, no: int, description: str):
        test_value = test_values[no - 1]

        expected_exception = test_value.expected_exception
        config_data = json.loads(test_value.config_data_str)

        with AppConfigFactory(config_data=config_data) as app_config_factory:
            if expected_exception:
                with pytest.raises(expected_exception):
                    app_config_factory.execute()
            else:
                app_config = app_config_factory.execute()
                assert app_config
