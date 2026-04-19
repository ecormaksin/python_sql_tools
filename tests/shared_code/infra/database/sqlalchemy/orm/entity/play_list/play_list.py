from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list.play_list_db_base import (
    PlayListDbBase,
)


class PlayList(PlayListDbBase):
    __tablename__ = "play_list"

    play_list_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"PlayList(play_list_id={self.play_list_id!r}, name={self.name!r})"
