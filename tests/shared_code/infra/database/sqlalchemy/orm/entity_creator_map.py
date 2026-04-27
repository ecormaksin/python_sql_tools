from typing import Any

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.album.album_db_entity_creator import (
    AlbumDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.artist.artist_db_entity_creator import (
    ArtistDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.customer.customer_db_entity_creator import (
    CustomerDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.employee.employee_db_entity_creator import (
    EmployeeDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.genre.genre_db_entity_creator import (
    GenreDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice.invoice_db_entity_creator import (
    InvoiceDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.media_type.media_type_db_entity_creator import (
    MediaTypeDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.play_list.play_list_db_entity_creator import (
    PlayListDbEntityCreator,
)


class EntityCreatorMap:
    @classmethod
    def get(cls) -> dict[str, AbstractDbEntityCreator]:
        return {
            "artist": ArtistDbEntityCreator,
            "genre": GenreDbEntityCreator,
            "media_type": MediaTypeDbEntityCreator,
            "album": AlbumDbEntityCreator,
            "play_list": PlayListDbEntityCreator,
            "employee": EmployeeDbEntityCreator,
            "customer": CustomerDbEntityCreator,
            "invoice": InvoiceDbEntityCreator,
        }
