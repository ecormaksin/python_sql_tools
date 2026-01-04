from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Artist(Base):
    __tablename__ = "artist"

    artist_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))

    def __repr__(self) -> str:
        return f"Artist(artist_id={self.artist_id!r}, name={self.name!r})"
