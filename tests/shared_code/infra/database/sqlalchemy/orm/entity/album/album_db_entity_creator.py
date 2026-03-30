from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base
from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.album import (
    Album,  # noqa: F401
)


class AlbumDbEntityCreator:
    @classmethod
    def execute(cls, engine: Engine):
        Base.metadata.create_all(engine)
