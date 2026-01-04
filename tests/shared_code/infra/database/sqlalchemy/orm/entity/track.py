from typing import Optional

from sqlalchemy import DECIMAL, ForeignKey, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Track(Base):
    __tablename__ = "track"

    track_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    album_id = mapped_column(ForeignKey("album.album_id"), nullable=True)
    media_type_id = mapped_column(ForeignKey("media_type.media_type_id"))
    genre_id = mapped_column(ForeignKey("genre.genre_id"), nullable=True)
    composer: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    milliseconds: Mapped[int] = mapped_column(Integer)
    bytes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    unit_price: Mapped[float] = mapped_column(DECIMAL(9, 2))

    __table_args__ = (
        Index("track_IX1", "name"),
        Index("track_IX2", "album_id"),
        Index("track_IX3", "genre_id"),
        Index("track_IX4", "media_type_id"),
        Index("track_IX5", "composer"),
    )

    def __repr__(self) -> str:
        return (
            "Track("
            "track_id={track_id!r}, "
            "name={name!r}, "
            "album_id={album_id!r}, "
            "media_type_id={media_type_id!r}, "
            "genre_id={genre_id!r}, "
            "composer={composer!r}, "
            "milliseconds={milliseconds!r}, "
            "bytes={bytes!r}, "
            "unit_price={unit_price!r}"
            ")"
        ).format(
            track_id=self.track_id,
            name=self.name,
            album_id=self.album_id,
            media_type_id=self.media_type_id,
            genre_id=self.genre_id,
            composer=self.composer,
            milliseconds=self.milliseconds,
            bytes=self.bytes,
            unit_price=self.unit_price,
        )
