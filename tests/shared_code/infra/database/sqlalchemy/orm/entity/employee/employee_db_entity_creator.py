from sqlalchemy import Engine

from tests.shared_code.infra.database.sqlalchemy.orm.entity.abstract_db_entity_creator import (
    AbstractDbEntityCreator,
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.employee.employee import (
    Employee,  # noqa: F401
)
from tests.shared_code.infra.database.sqlalchemy.orm.entity.employee.employee_db_base import (
    EmployeeDbBase,
)


class EmployeeDbEntityCreator(AbstractDbEntityCreator):
    @classmethod
    def execute(cls, engine: Engine):
        EmployeeDbBase.metadata.create_all(engine)
