import datetime
import tempfile
import traceback
from pathlib import Path
from typing import Optional

from ulid import ULID

from shared_code.infra.file_system.directory_creator import DirectoryCreator


class AppDirectoryCreator:
    @classmethod
    def execute(
        cls, module_name: str, directory_type: str, directory_path_str: Optional[str]
    ) -> str:
        dir_path_str = directory_path_str

        if not dir_path_str:
            now = datetime.datetime.now()
            dir_path_str = str(
                Path(tempfile.gettempdir())
                .joinpath("python_sql_tools")
                .joinpath(module_name)
                .joinpath(now.strftime("%Y%m%d-%H%M%S") + "-" + str(ULID()))
            )

        try:
            DirectoryCreator.execute(path_str=dir_path_str)
        except IOError | PermissionError:
            stacktrace_str = traceback.format_exc()
            raise RuntimeError(
                f"Cannot create {directory_type} directory '{dir_path_str}'. detail: {stacktrace_str}"
            )

        return dir_path_str
