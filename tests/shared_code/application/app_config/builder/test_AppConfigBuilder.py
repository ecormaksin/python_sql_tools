import json
from dataclasses import dataclass
from typing import Optional, Type

import pytest

from shared_code.application.app_config.builder.entity import AppConfigBuilder


@dataclass(frozen=True)
class Item:
    config_data_str: str
    expected_exception: Optional[Type[Exception]]


default_valid_app_config_str = """
{
  "target_sheet_names": "",
  "exclude_sheet_names": "",
  "table_name_cell": {
    "row": 1,
    "column": 1
  },
  "column_name_row": 1,
  "column_default_row": 3,
  "nullable_column_flag_row": 4,
  "data_type_row": 5,
  "key_position_row": 6,
  "no_quotation_row": 7,
  "data_start_cell": {
    "row": 8,
    "column": 4
  },
  "set_empty_string_instead_of_null": true,
  "number_of_lines_per_file": -1
}
"""

default_valid_app_config = json.loads(default_valid_app_config_str)

table_name_cell_missing = dict(default_valid_app_config)
del table_name_cell_missing["table_name_cell"]

table_name_cell_row_invalid = dict(default_valid_app_config)
table_name_cell_row_invalid |= {"table_name_cell": {"row": 0}}

table_name_cell_col_invalid = dict(default_valid_app_config)
table_name_cell_col_invalid |= {"table_name_cell": {"col": 0}}

column_name_row_invalid = dict(default_valid_app_config)
column_name_row_invalid |= {"column_name_row": 0}

data_type_row_invalid = dict(default_valid_app_config)
data_type_row_invalid |= {"data_type_row": 0}

data_start_cell_row_invalid = dict(default_valid_app_config)
data_start_cell_row_invalid |= {"data_start_cell": {"row": 0}}

data_start_cell_col_invalid = dict(default_valid_app_config)
data_start_cell_col_invalid |= {"data_start_cell": {"col": 0}}

number_of_lines_per_file_invalid = dict(default_valid_app_config)
number_of_lines_per_file_invalid |= {"number_of_lines_per_file": -2}

number_of_lines_per_file_valid = dict(default_valid_app_config)
number_of_lines_per_file_valid |= {"number_of_lines_per_file": 10}

key_position_row_invalid = dict(default_valid_app_config)
key_position_row_invalid |= {"key_position_row": 0}

no_quotation_row_invalid = dict(default_valid_app_config)
no_quotation_row_invalid |= {"no_quotation_row": 0}

target_sheet_names_exclude_sheet_names_specified = dict(default_valid_app_config)
target_sheet_names_exclude_sheet_names_specified |= {
    "target_sheet_names": "sheet_A,",
    "exclude_sheet_names": "sheet_B,",
}

target_sheet_names_specified = dict(default_valid_app_config)
target_sheet_names_specified |= {"target_sheet_names": "sheet_A,"}

exclude_sheet_names_specified = dict(default_valid_app_config)
exclude_sheet_names_specified |= {"exclude_sheet_names": "sheet_B,"}

same_sheets_specified_in_target_exclude = dict(default_valid_app_config)
same_sheets_specified_in_target_exclude |= {
    "target_sheet_names": "sheet_A,sheet_C,",
    "exclude_sheet_names": "sheet_B,sheet_A,",
}

set_empty_string_instead_of_null_is_not_bool = dict(default_valid_app_config)
set_empty_string_instead_of_null_is_not_bool |= {
    "set_empty_string_instead_of_null": "a"
}

set_empty_string_instead_of_null_is_valid = dict(default_valid_app_config)
set_empty_string_instead_of_null_is_valid |= {"set_empty_string_instead_of_null": True}

test_params = [
    ("no properties", Item(config_data_str="{}", expected_exception=RuntimeError)),
    (
        "'table_name_cell' missing",
        Item(
            config_data_str=json.dumps(table_name_cell_missing),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'table_name_cell's row invalid",
        Item(
            config_data_str=json.dumps(table_name_cell_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'table_name_cell's column invalid",
        Item(
            config_data_str=json.dumps(table_name_cell_col_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'column_name_row' invalid",
        Item(
            config_data_str=json.dumps(column_name_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'data_type_row' invalid",
        Item(
            config_data_str=json.dumps(data_type_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'data_start_cell's row invalid",
        Item(
            config_data_str=json.dumps(data_start_cell_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'data_start_cell's column invalid",
        Item(
            config_data_str=json.dumps(data_start_cell_col_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'number_of_lines_per_file' invalid",
        Item(
            config_data_str=json.dumps(number_of_lines_per_file_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'number_of_lines_per_file' valid",
        Item(
            config_data_str=json.dumps(number_of_lines_per_file_valid),
            expected_exception=None,
        ),
    ),
    (
        "'key_position_row' invalid",
        Item(
            config_data_str=json.dumps(key_position_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'no_quotation_row' invalid",
        Item(
            config_data_str=json.dumps(no_quotation_row_invalid),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "both 'target_sheet_names' and 'exclude_sheet_names' specified",
        Item(
            config_data_str=json.dumps(
                target_sheet_names_exclude_sheet_names_specified
            ),
            expected_exception=None,
        ),
    ),
    (
        "'target_sheet_names' specified",
        Item(
            config_data_str=json.dumps(target_sheet_names_specified),
            expected_exception=None,
        ),
    ),
    (
        "'exclude_sheet_names' specified",
        Item(
            config_data_str=json.dumps(exclude_sheet_names_specified),
            expected_exception=None,
        ),
    ),
    (
        "same sheets specified in 'target_sheet_names' and 'exclude_sheet_names'",
        Item(
            config_data_str=json.dumps(same_sheets_specified_in_target_exclude),
            expected_exception=RuntimeError,
        ),
    ),
    (
        "'set_empty_string_instead_of_null' is not bool",
        Item(
            config_data_str=json.dumps(set_empty_string_instead_of_null_is_not_bool),
            expected_exception=ValueError,
        ),
    ),
    (
        "'set_empty_string_instead_of_null' is valid",
        Item(
            config_data_str=json.dumps(set_empty_string_instead_of_null_is_valid),
            expected_exception=None,
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
