from pathlib import Path


class DirectoryCreator:
    @classmethod
    def execute(cls, path_str: str):
        dir_path = Path(path_str)

        if dir_path.exists() and dir_path.is_dir():
            return

        dir_path.mkdir(parents=True, exist_ok=True)
