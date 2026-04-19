from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.album import (
    Album,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.album_db_base import (
    AlbumDbBase,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.track import (
    Track,  # noqa: F401
)


class AlbumDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        AlbumDbBase.metadata.create_all(engine)
