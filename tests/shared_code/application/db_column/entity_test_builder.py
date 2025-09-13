from typing import Optional

from shared_code.domain.db_column.column_default import ColumnDefault
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag


class DBColumnTestBuilder:
    @classmethod
    def execute(cls, source_str: str) -> DBColumn:
        rows = source_str.splitlines()

        column_default = cls.__clean_value(rows[1])
        key_position = cls.__clean_value(rows[4])
        no_quotation = cls.__clean_value(rows[5])

        return DBColumn(
            column_name=ColumnName(cls.__clean_value(rows[0])),
            column_default=ColumnDefault(column_default) if column_default else None,
            nullable_column_flag=NullableColumnFlag.from_str(
                cls.__clean_value(rows[2])
            ),
            data_type=DataType(cls.__clean_value(rows[3])),
            key_position=KeyPosition.from_str(key_position) if key_position else None,
            no_quotation=NoQuotation(no_quotation) if no_quotation else None,
        )

    @classmethod
    def __clean_value(cls, row_data: str) -> Optional[str]:
        cleaned_value = row_data.strip()
        return None if cleaned_value == "None" else cleaned_value
