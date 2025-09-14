from dataclasses import dataclass
from typing import Optional

import pytest

from shared_code.domain.db_column.column_default import ColumnDefault
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag
from tests.shared_code.application.db_column.entity_test_builder import (
    DBColumnTestBuilder,
)


@dataclass(frozen=True)
class Item:
    db_column_source_str: str
    expected_db_column: Optional[DBColumn]


test_params = [
    (
        "key int column without default value",
        Item(
            db_column_source_str="""
            {
                "column_name": "ID",
                "column_default": "None",
                "nullable_column_flag": "NO",
                "data_type": "@INT",
                "key_position": 1,
                "no_quotation": "None"
            }
            """,
            expected_db_column=DBColumn(
                column_name=ColumnName("ID"),
                column_default=None,
                nullable_column_flag=NullableColumnFlag.NO,
                data_type=DataType("@INT"),
                key_position=KeyPosition(1),
                no_quotation=None,
            ),
        ),
    ),
    (
        "required varchar column without default value",
        Item(
            db_column_source_str="""
            {
                "column_name": "required_varchar_column",
                "column_default": "None",
                "nullable_column_flag": "NO",
                "data_type": "@VARCHAR(50)",
                "key_position": "None",
                "no_quotation": "○"
            }
            """,
            expected_db_column=DBColumn(
                column_name=ColumnName("required_varchar_column"),
                column_default=None,
                nullable_column_flag=NullableColumnFlag.NO,
                data_type=DataType("@VARCHAR(50)"),
                key_position=None,
                no_quotation=NoQuotation("○"),
            ),
        ),
    ),
    (
        "optional varchar column with default value",
        Item(
            db_column_source_str="""
            {
                "column_name": "optional_varchar_column",
                "column_default": "test_default_value",
                "nullable_column_flag": "YES",
                "data_type": "@VARCHAR(50)",
                "key_position": "None",
                "no_quotation": "○"
            }
            """,
            expected_db_column=DBColumn(
                column_name=ColumnName("optional_varchar_column"),
                column_default=ColumnDefault("test_default_value"),
                nullable_column_flag=NullableColumnFlag.YES,
                data_type=DataType("@VARCHAR(50)"),
                key_position=None,
                no_quotation=NoQuotation("○"),
            ),
        ),
    ),
]


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        actual = DBColumnTestBuilder.from_json_str(test_value.db_column_source_str)

        expected = test_value.expected_db_column

        assert actual == expected