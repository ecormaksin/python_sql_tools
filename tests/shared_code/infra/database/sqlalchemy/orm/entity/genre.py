from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Genre(genre_id={self.genre_id!r}, name={self.name!r})"
