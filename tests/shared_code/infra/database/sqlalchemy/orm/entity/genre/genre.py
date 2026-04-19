from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.genre.genre_db_base import (
    GenreDbBase,
)


class Genre(GenreDbBase):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Genre(genre_id={self.genre_id!r}, name={self.name!r})"
