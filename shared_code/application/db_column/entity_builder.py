from typing import Optional

from shared_code.domain.app_config import AppConfig
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation

from dataclasses import dataclass

from shared_code.domain.row_number import RowNumber


@dataclass(frozen=True)
class DBColumnBuildRequest:
    source_data: list[str]
    app_config: AppConfig


class DBColumnBuilder:
    @classmethod
    def execute(cls, a_request: DBColumnBuildRequest) -> Optional[DBColumn]:
        source_data = a_request.source_data
        app_config = a_request.app_config

        column_name_str = cls.__get_value(
            source_data=source_data, row_number=app_config.db_column_name_row_number
        )
        if not column_name_str or column_name_str == "None":
            return None

        data_type_str = cls.__get_value(
            source_data=source_data, row_number=app_config.data_type_row_number
        )
        if not data_type_str:
            return None

        key_position_str = cls.__get_value(
            source_data=source_data, row_number=app_config.key_position_row_number
        )
        no_quotation_str = cls.__get_value(
            source_data=source_data, row_number=app_config.no_quotation_row_number
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

    @staticmethod
    def __get_value(source_data: list[str], row_number: Optional[RowNumber]) -> str:
        if not row_number:
            return ""

        value_str = source_data[row_number.value - 1]
        return "" if value_str == "None" else value_str
