from dataclasses import dataclass
from typing import Optional, Type

import pytest

from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag


@dataclass(frozen=True)
class Item:
    flag_value: str
    expected_exception: Optional[Type[Exception]]


test_params = [
    ("valid as Yes", Item(flag_value="YES", expected_exception=None)),
    ("valid as Yes", Item(flag_value="yes", expected_exception=None)),
    ("valid as No", Item(flag_value="NO", expected_exception=None)),
    ("invalid value", Item(flag_value="true", expected_exception=KeyError)),
]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        flag_value = test_value.flag_value
        expected_exception = test_value.expected_exception

        if expected_exception:
            with pytest.raises(expected_exception):
                NullableColumnFlag.from_str_value(flag_value)
        else:
            nullable_column_flag = NullableColumnFlag.from_str_value(flag_value)
            assert nullable_column_flag
