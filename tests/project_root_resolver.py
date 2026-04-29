from pathlib import Path

class ProjectRootResolver:
    @classmethod
    def execute(cls, start: Path) -> Path:
        for parent in [start, *start.parents]:
            if parent.joinpath("pyproject.toml").exists():
                return parent

        raise RuntimeError("プロジェクトルートが見つかりませんでした。")
