from shared_code.domain.app_config import AppConfig
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation

from dataclasses import dataclass


@dataclass(frozen=True)
class DBColumnBuildRequest:
    source_data: list[str]
    app_config: AppConfig


class DBColumnBuilder:
    @classmethod
    def execute(cls, a_request: DBColumnBuildRequest) -> DBColumn:
        source_data = a_request.source_data
        app_config = a_request.app_config

        column_name_str = source_data[app_config.db_column_name_row_number.value - 1]
        data_type_str = source_data[app_config.data_type_row_number.value - 1]

        key_position_row_number = app_config.key_position_row_number
        key_position_str = (
            source_data[key_position_row_number.value - 1]
            if key_position_row_number
            else ""
        )

        no_quotation_row_number = app_config.no_quotation_row_number
        no_quotation_str = (
            source_data[no_quotation_row_number.value - 1]
            if no_quotation_row_number
            else ""
        )

        return DBColumn(
            column_name=ColumnName(value=column_name_str),
            data_type=DataType(value=data_type_str),
            key_position=KeyPosition(value=key_position_str)
            if key_position_str
            else None,
            no_quotation=NoQuotation(value=no_quotation_str)
            if no_quotation_str
            else None,
        )
