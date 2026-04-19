from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist import (
    Artist,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist_db_base import (
    ArtistDbBase,
)


class ArtistDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        ArtistDbBase.metadata.create_all(engine)
