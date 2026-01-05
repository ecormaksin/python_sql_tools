from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.album import (
    Album,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist import (
    Artist,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base
from tests.shared_code.infra.database.sqlalchemy.orm.entity.customer import (
    Customer,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.employee import (
    Employee,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.genre import (
    Genre,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice import (
    Invoice,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice_line import (
    InvoiceLine,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.media_type import (
    MediaType,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list import (
    PlayList,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.playlist_track import (
    PlayListTrack,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.track import (
    Track,  # noqa: F401
)


class EntityCreator:
    @classmethod
    def execute(cls, engine: Engine):
        Base.metadata.create_all(engine)
