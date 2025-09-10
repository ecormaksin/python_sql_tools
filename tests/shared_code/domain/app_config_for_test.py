import json
from typing import Any


class AppConfigForTest:
    VALID_SAMPLE_DATA_STR: str = """
{
  "table_name_cell": {
    "row": 1,
    "column": 1
  },
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

    @classmethod
    def get_config_data(cls, data_str: str) -> dict[str, Any]:
        return json.loads(data_str)
