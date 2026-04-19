from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.customer.customer import (
    Customer,
)  # noqa: F401
from tests.shared_code.infra.database.sqlalchemy.orm.entity.customer.customer_db_base import (
    CustomerDbBase,
)


class CustomerDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        CustomerDbBase.metadata.create_all(engine)
