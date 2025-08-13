from pathlib import Path


class FileExistenceChecker:
    @classmethod
    def exists(cls, file_path) -> bool:
        a_path = Path(file_path)
        return True if a_path.exists() and a_path.is_file() else False

    @classmethod
    def not_exists(cls, file_path) -> bool:
        return not cls.exists(file_path=file_path)
