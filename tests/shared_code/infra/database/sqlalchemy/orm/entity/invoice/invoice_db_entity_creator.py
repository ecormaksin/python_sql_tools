from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice.invoice import (
    Invoice,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice.invoice_db_base import (
    InvoiceDbBase,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.invoice.invoice_line import (
    InvoiceLine,  # noqa: F401
)


class InvoiceDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        InvoiceDbBase.metadata.create_all(engine)
