from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list.play_list import (
    PlayList,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list.play_list_db_base import (
    PlayListDbBase,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list.playlist_track import (
    PlayListTrack,  # noqa: F401
)


class PlayListDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        PlayListDbBase.metadata.create_all(engine)
