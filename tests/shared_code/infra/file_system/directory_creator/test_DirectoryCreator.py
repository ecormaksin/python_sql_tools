import os
from dataclasses import dataclass
from typing import Optional, Type

import pytest

from shared_code.infra.file_system.directory_creator import DirectoryCreator

test_params = ["directory exists", "directory does not exist even after creation"]


@dataclass(frozen=True)
class Item:
    dir_path_str: str
    expected_exception: Optional[Type[Exception]]


if os.name == "nt":
    test_values = [
        Item(dir_path_str="C:\\temp", expected_exception=None),
        Item(dir_path_str="ZZ:\\temp", expected_exception=OSError),
    ]
else:
    test_values = [
        Item(dir_path_str="/tmp", expected_exception=None),
        Item(dir_path_str="/sys/tmp", expected_exception=PermissionError),
    ]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, description) for index, (description) in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_values[no - 1]

        expected_exception = test_value.expected_exception
        path_str = test_value.dir_path_str

        if expected_exception:
            with pytest.raises(expected_exception):
                DirectoryCreator.execute(path_str=path_str)
        else:
            DirectoryCreator.execute(path_str=path_str)