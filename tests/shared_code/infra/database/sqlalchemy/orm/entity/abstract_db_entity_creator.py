from abc import ABC
from sqlalchemy import Engine
from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base

class AbstractDbEntityCreator(ABC):
    @classmethod
    def execute(cls, engine: Engine):
        Base.metadata.create_all(engine)
