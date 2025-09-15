from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional

import pytest

from shared_code.application.dml.value_build_request import DMLValueBuildRequest
from shared_code.application.dml.value_builder import DMLValueBuilder
from shared_code.domain.set_empty_str_instead_of_null import SetEmptyStrInsteadOfNull
from tests.shared_code.application.db_column.entity_test_builder import (
    DBColumnTestBuilder,
)


@dataclass(frozen=True)
class Item:
    test_case_no: str
    db_column_dict: dict[str, Any]
    cell_value: Optional[str]
    set_empty_str_instead_of_null_value: bool
    expected: str


column_base_dict = {"column_name": "test_column", "key_position": 1}


@dataclass(frozen=True)
class DescriptionDictPair:
    description: str
    dict_obj: dict[str, Any]


@dataclass(frozen=True)
class DescriptionBoolPair:
    description: str
    bool_value: bool


class DescriptionEnumBase:
    @classmethod
    def from_description(cls, description: str):
        for member in cls:
            if member.value.description == description:
                return member
        raise KeyError(f"'{description}' is not found.")


class ParamColumnTypeQuote(DescriptionEnumBase, Enum):
    UNICODE = DescriptionDictPair("必要_Unicode", {"data_type": "NVARCHAR(100)"})
    NON_UNICODE = DescriptionDictPair("必要_非Unicode", {"data_type": "VARCHAR(100)"})
    NO_QUOTE = DescriptionDictPair("不要", {"data_type": "INT"})


class ParamColumnDefault(DescriptionEnumBase, Enum):
    WITH_QUOTE = DescriptionDictPair(
        "あり_引用符あり", {"column_default": "test_default_value"}
    )
    WITHOUT_QUOTE = DescriptionDictPair("あり_引用符なし", {"column_default": "9999"})
    NO_VALUE = DescriptionDictPair("なし", {"column_default": "None"})


class ParamNullableColumn(DescriptionEnumBase, Enum):
    YES = DescriptionDictPair("任意", {"nullable_column_flag": "YES"})
    NO = DescriptionDictPair("必須", {"nullable_column_flag": "NO"})


class ParamAddQuoteToColumnValue(DescriptionEnumBase, Enum):
    YES = DescriptionDictPair("あり", {"no_quotation": "None"})
    NO = DescriptionDictPair("なし", {"no_quotation": "○"})


class ParamSetEmptyStrInsteadOfNull(DescriptionEnumBase, Enum):
    YES = DescriptionBoolPair("する", True)
    NO = DescriptionBoolPair("しない", False)


test_data_raw_str = """
1	必要_Unicode	あり_引用符あり	任意	あり	None	する	None	N'test_default_value'
2	必要_Unicode	あり_引用符あり	任意	あり	長さ0の文字列	する	''	N'test_default_value'
3	必要_Unicode	あり_引用符あり	必須	なし	あり	しない	test_column_value	test_column_value
4	必要_Unicode	あり_引用符あり	必須	あり	None文字列	しない	'None'	N'test_default_value'
5	必要_Unicode	なし	任意	なし	あり	する	test_column_value	test_column_value
6	必要_非Unicode	あり_引用符あり	任意	あり	あり	しない	test_column_value	'test_column_value'
7	必要_非Unicode	あり_引用符あり	任意	なし	長さ0の文字列	しない	''	test_default_value
8	必要_非Unicode	なし	必須	あり	None文字列	する	'None'	''
9	必要_非Unicode	なし	必須	なし	None	しない	None	''
10	不要	あり_引用符なし	任意	なし	None	しない	None	9999
11	不要	あり_引用符なし	任意	なし	None文字列	しない	'None'	9999
12	不要	あり_引用符なし	任意	なし	あり	しない	1	1
13	不要	あり_引用符なし	必須	なし	長さ0の文字列	しない	''	9999
14	不要	なし	必須	なし	長さ0の文字列	しない	''	null
"""

cell_value_map: dict[str, Any] = {"None": None, "'None'": "None", "''": ""}

test_params = []

test_data_rows = test_data_raw_str.splitlines()
for test_data_row in test_data_rows:
    if not test_data_row.strip():
        continue

    test_data_cells = test_data_row.split("\t")

    column_type_quote = ParamColumnTypeQuote.from_description(test_data_cells[1])
    column_default = ParamColumnDefault.from_description(test_data_cells[2])
    nullable_column = ParamNullableColumn.from_description(test_data_cells[3])
    add_quote_to_column_value = ParamAddQuoteToColumnValue.from_description(
        test_data_cells[4]
    )
    param_set_empty_str_instead_of_null = (
        ParamSetEmptyStrInsteadOfNull.from_description(test_data_cells[6])
    )

    cell_value = test_data_cells[7]
    if cell_value in cell_value_map:
        cell_value = cell_value_map[cell_value]

    expected = test_data_cells[8]

    test_param = Item(
        test_case_no=test_data_cells[0],
        db_column_dict=column_base_dict
        | column_type_quote.value.dict_obj
        | column_default.value.dict_obj
        | nullable_column.value.dict_obj
        | add_quote_to_column_value.value.dict_obj,
        cell_value=cell_value,
        set_empty_str_instead_of_null_value=param_set_empty_str_instead_of_null.value.bool_value,
        expected=expected,
    )

    test_params.append(test_param)


class TestClass:
    @pytest.mark.parametrize(
        "no",
        [(index + 1) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int):
        test_value = test_params[no - 1]

        a_request = DMLValueBuildRequest(
            db_column=DBColumnTestBuilder.from_dict(test_value.db_column_dict),
            cell_value=test_value.cell_value,
            set_empty_str_instead_of_null=SetEmptyStrInsteadOfNull(
                test_value.set_empty_str_instead_of_null_value
            ),
        )

        actual = DMLValueBuilder.execute(a_request=a_request)

        assert actual == test_value.expected