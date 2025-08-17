from dataclasses import dataclass
from pathlib import Path

import pytest

from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


@dataclass(frozen=True)
class Item:
    file_name: str
    expected: bool


test_params = [
    ("file exists", Item(file_name="dummy.txt", expected=True)),
    ("file does not exist", Item(file_name="dummy_a.txt", expected=False)),
]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        file_path = Path(__file__).parent.joinpath(test_value.file_name)
        assert FileExistenceChecker.exists(file_path=file_path) == test_value.expected
