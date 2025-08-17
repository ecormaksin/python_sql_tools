from dataclasses import dataclass

from shared_code.application.db_column.entity_builder import (
    DBColumnBuildRequest,
    DBColumnBuilder,
)
from shared_code.domain.app_config import AppConfig
from shared_code.domain.db_column.list import DBColumns


@dataclass(frozen=True)
class DBColumnsBuildRequest:
    source_data: list[list[str]]
    app_config: AppConfig


class DBColumnsBuilder:
    @classmethod
    def execute(cls, a_request: DBColumnsBuildRequest) -> DBColumns:
        source_data = a_request.source_data
        app_config = a_request.app_config

        db_columns = DBColumns.empty()

        for element_data in source_data:
            element_request = DBColumnBuildRequest(
                source_data=element_data, app_config=app_config
            )
            db_column = DBColumnBuilder.execute(a_request=element_request)

            db_columns = db_columns.append(element=db_column)

        return db_columns
