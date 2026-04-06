from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base


class PlayListTrack(Base):
    __tablename__ = "playlist_track"

    play_list_id = mapped_column(ForeignKey("play_list.play_list_id"), primary_key=True)
    track_id = mapped_column(ForeignKey("track.track_id"), primary_key=True)

    __table_args__ = (Index("playlist_track_IX1", "track_id"),)

    def __repr__(self) -> str:
        return f"PlayListTrack(play_list_id={self.play_list_id!r}, track_id={self.track_id!r})"
