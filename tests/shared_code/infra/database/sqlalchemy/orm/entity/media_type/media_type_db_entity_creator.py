from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.media_type.media_type import (
    MediaType,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.media_type.media_type_db_base import (
    MediaTypeDbBase,
)


class MediaTypeDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        MediaTypeDbBase.metadata.create_all(engine)
