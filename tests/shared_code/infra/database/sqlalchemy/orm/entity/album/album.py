from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.album_db_base import (
    AlbumDbBase,
)


class Album(AlbumDbBase):
    __tablename__ = "album"

    album_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(160))
    artist_id = mapped_column(ForeignKey("artist.artist_id"))

    __table_args__ = (Index("album_IX1", "artist_id"),)

    def __repr__(self) -> str:
        return f"Album(album_id={self.album_id!r}, title={self.title!r}, artist_id={self.artist_id!r})"
