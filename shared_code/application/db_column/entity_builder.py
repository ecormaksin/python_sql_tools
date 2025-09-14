from dataclasses import dataclass
from typing import Optional

from shared_code.domain.app_config import AppConfig
from shared_code.domain.db_column.column_default import ColumnDefault
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag
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
        if not column_name_str:
            return None

        nullable_column_flag_str = cls.__get_value(
            source_data=source_data,
            row_number=app_config.nullable_column_flag_row_number,
        )
        if not nullable_column_flag_str:
            return None

        data_type_str = cls.__get_value(
            source_data=source_data, row_number=app_config.data_type_row_number
        )
        if not data_type_str:
            return None

        column_default_str = cls.__get_value(
            source_data=source_data, row_number=app_config.column_default_row_number
        )
        key_position_str = cls.__get_value(
            source_data=source_data, row_number=app_config.key_position_row_number
        )
        no_quotation_str = cls.__get_value(
            source_data=source_data, row_number=app_config.no_quotation_row_number
        )

        return DBColumn(
            column_name=ColumnName(value=column_name_str),
            column_default=ColumnDefault(value=column_default_str)
            if column_default_str
            else None,
            nullable_column_flag=NullableColumnFlag.from_str(nullable_column_flag_str),
            data_type=DataType(value=data_type_str),
            key_position=KeyPosition.from_str(str_value=key_position_str)
            if key_position_str
            else None,
            no_quotation=NoQuotation(value=no_quotation_str)
            if no_quotation_str
            else None,
        )

    @staticmethod
    def __get_value(source_data: list[str], row_number: RowNumber) -> Optional[str]:
        value_str = source_data[row_number.value - 1]
        return None if (not value_str or value_str == "None") else value_str
