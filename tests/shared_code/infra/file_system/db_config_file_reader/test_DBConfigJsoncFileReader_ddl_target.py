from dataclasses import dataclass
from pathlib import Path

import pytest

from shared_code.domain.ddl.create_target.map import DDLCreateTargetMap
from shared_code.infra.file_system.db_config_jsonc_file_reader import (
    DBConfigJsoncFileReader,
)


@dataclass(frozen=True)
class Item:
    file_name: str
    expected: DDLCreateTargetMap


test_pattern_1 = [
    (
        "with ddl target",
        Item(
            file_name="with_ddl_target.json",
            expected=DDLCreateTargetMap.from_dict_list(
                dict_list=[
                    {"schema": "db2"},
                    {"schema": "db3", "include_tables": ["table1", "table2"]},
                    {"schema": "db4", "exclude_tables": ["table3"]},
                    {
                        "schema": "db5",
                        "include_tables": ["table4", "table5"],
                        "exclude_tables": ["table6", "table7"],
                    },
                ]
            ),
        ),
    )
]

test_pattern_2 = [
    (
        "without ddl target",
        Item(
            file_name="without_ddl_target.json",
            expected=DDLCreateTargetMap.from_dict_list(dict_list=[{"schema": "db1"}]),
        ),
    )
]


test_params = test_pattern_1 + test_pattern_2


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        file_path = (
            Path(__file__).parent.joinpath("test_data").joinpath(test_value.file_name)
        )

        actual = DBConfigJsoncFileReader.get_ddl_create_target_map(
            db_config_file_path_str=str(file_path)
        )

        assert actual == test_value.expected
