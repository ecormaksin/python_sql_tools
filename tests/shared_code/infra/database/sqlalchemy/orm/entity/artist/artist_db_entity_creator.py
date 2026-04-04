from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base
from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist import Artist # noqa: F401
from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import AbstractDbEntityCreator

class ArtistDbEntityCreator(AbstractDbEntityCreator):
    pass
