import json
from typing import Any


class AppConfigForTest:
    VALID_SAMPLE_DATA_STR: str = """
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

    @classmethod
    def get_config_data(cls, data_str: str) -> dict[str, Any]:
        return json.loads(data_str)
