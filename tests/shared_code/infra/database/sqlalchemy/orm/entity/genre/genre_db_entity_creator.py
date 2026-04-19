from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.genre.genre import (
    Genre,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.genre.genre_db_base import (
    GenreDbBase,
)


class GenreDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        GenreDbBase.metadata.create_all(engine)
