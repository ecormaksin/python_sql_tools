from pathlib import Path
from typing import Optional, Union

from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class AppFileUtils:
    @classmethod
    def determine_and_check(
        cls, arg_file_path_str: Optional[str], default_file_path: Union[str, Path]
    ) -> str:
        file_path_str = arg_file_path_str

        if not file_path_str:
            file_path_str = default_file_path
            if type(file_path_str) is Path:
                file_path_str = str(file_path_str)

        if FileExistenceChecker.not_exists(file_path=file_path_str):
            raise RuntimeError(f"'{file_path_str}' does not exist.")

        return file_path_str
