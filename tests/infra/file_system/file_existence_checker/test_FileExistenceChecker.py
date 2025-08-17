from dataclasses import dataclass
from pathlib import Path

import pytest

from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker

test_params = list(enumerate(["file exists", "file does not exist"]))


@dataclass(frozen=True)
class Item:
    file_name: str
    expected: bool


test_values = [
    Item(file_name="dummy.txt", expected=True),
    Item(file_name="dummy_a.txt", expected=False),
]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, description) for index, (description) in test_params],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_values[no - 1]

        file_path = Path(__file__).parent.joinpath(test_value.file_name)
        assert FileExistenceChecker.exists(file_path=file_path) == test_value.expected
