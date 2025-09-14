import json
from typing import Any, Optional

from shared_code.domain.db_column.column_default import ColumnDefault
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag


class DBColumnTestBuilder:
    @classmethod
    def from_json_str(cls, json_str: str) -> DBColumn:
        dict_obj = json.loads(json_str)
        return cls.from_dict(dict_obj)

    @classmethod
    def from_dict(cls, dict_obj: dict[str, Any]) -> DBColumn:
        column_default = cls.__clean_value(dict_obj["column_default"])
        key_position = cls.__clean_value(str(dict_obj["key_position"]))
        no_quotation = cls.__clean_value(dict_obj["no_quotation"])

        return DBColumn(
            column_name=ColumnName(dict_obj["column_name"]),
            column_default=ColumnDefault(column_default) if column_default else None,
            nullable_column_flag=NullableColumnFlag.from_str(
                dict_obj["nullable_column_flag"]
            ),
            data_type=DataType(dict_obj["data_type"]),
            key_position=KeyPosition.from_str(key_position) if key_position else None,
            no_quotation=NoQuotation(no_quotation) if no_quotation else None,
        )

    @classmethod
    def __clean_value(cls, prop_data: str) -> Optional[str]:
        cleaned_value = prop_data.strip()
        return None if cleaned_value == "None" else cleaned_value
