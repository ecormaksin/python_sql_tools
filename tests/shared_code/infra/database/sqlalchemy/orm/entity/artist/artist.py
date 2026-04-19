from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist_db_base import (
    ArtistDbBase,
)


class Artist(ArtistDbBase):
    __tablename__ = "artist"

    artist_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))

    def __repr__(self) -> str:
        return f"Artist(artist_id={self.artist_id!r}, name={self.name!r})"
