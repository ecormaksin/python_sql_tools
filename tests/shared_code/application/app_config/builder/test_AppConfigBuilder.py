import json
from dataclasses import dataclass
from typing import Optional, Type

import pytest

from shared_code.application.app_config.builder.entity import AppConfigBuilder


@dataclass(frozen=True)
class Item:
    config_data_str: str
    expected_exception: Optional[Type[Exception]]


test_params = [
    ("no properties", Item(config_data_str="{}", expected_exception=RuntimeError)),
    (
        "'table_name' missing",
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
    ),
    (
        "'table_name_cell' missing",
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
    ),
    (
        "'table_name_cell's row invalid",
        Item(
            config_data_str="""
    {
      "table_name": "cell",
      "table_name_cell": {
        "row": 0,
        "column": 1
      },
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
    ),
    (
        "'table_name_cell's column invalid",
        Item(
            config_data_str="""
    {
      "table_name": "cell",
      "table_name_cell": {
        "row": 1,
        "column": 0
      },
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
    ),
    (
        "'table_name's value not defined",
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
    ),
    (
        "'column_name_row' invalid",
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
    ),
    (
        "'data_type_row' invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 0,
  "data_start_cell": {
    "row": 6,
    "column": 2
  }
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'data_start_cell's row invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 0,
    "column": 2
  }
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'data_start_cell's column invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 0
  }
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'number_of_lines_per_file' invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": -2
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'number_of_lines_per_file' valid",
        Item(
            config_data_str="""
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
  "number_of_lines_per_file": 10
}
""",
            expected_exception=None,
        ),
    ),
    (
        "'key_position_row' invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "key_position_row": 0,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'no_quotation_row' invalid",
        Item(
            config_data_str="""
{
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "no_quotation_row": 0,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=RuntimeError,
        ),
    ),
    (
        "both 'target_sheet_names' and 'exclude_sheet_names' specified",
        Item(
            config_data_str="""
{
  "target_sheet_names": "sheet_A,",
  "exclude_sheet_names": "sheet_B,",
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "no_quotation_row": 4,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=None,
        ),
    ),
    (
        "'target_sheet_names' specified",
        Item(
            config_data_str="""
{
  "target_sheet_names": "sheet_A,",
  "exclude_sheet_names": "",
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "no_quotation_row": 4,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=None,
        ),
    ),
    (
        "'exclude_sheet_names' specified",
        Item(
            config_data_str="""
{
  "target_sheet_names": "",
  "exclude_sheet_names": "sheet_B,",
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "no_quotation_row": 4,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=None,
        ),
    ),
    (
        "same sheets specified in 'target_sheet_names' and 'exclude_sheet_names'",
        Item(
            config_data_str="""
{
  "target_sheet_names": "sheet_A,sheet_C,",
  "exclude_sheet_names": "sheet_B,sheet_A,",
  "table_name": "sheet",
  "column_name_row": 1,
  "data_type_row": 3,
  "no_quotation_row": 4,
  "data_start_cell": {
    "row": 6,
    "column": 2
  },
  "number_of_lines_per_file": 10
}
""",
            expected_exception=RuntimeError,
        ),
    ),
]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        expected_exception = test_value.expected_exception
        config_data = json.loads(test_value.config_data_str)

        with AppConfigBuilder(config_data=config_data) as app_config_builder:
            if expected_exception:
                with pytest.raises(expected_exception):
                    app_config_builder.execute()
            else:
                app_config = app_config_builder.execute()
                assert app_config
