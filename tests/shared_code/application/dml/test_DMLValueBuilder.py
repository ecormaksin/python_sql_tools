from dataclasses import dataclass
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
    db_column_dict: dict[str, Any]
    cell_value: Optional[str]
    set_empty_str_instead_of_null_value: bool
    expected: str


column_base_dict = {"column_name": "test_column", "key_position": 1}

unicode_column_data_type_dict = {"data_type": "NVARCHAR(100)"}
non_unicode_column_data_type_dict = {"data_type": "VARCHAR(100)"}
no_quote_column_data_type_dict = {"data_type": "INT"}

column_default_no_value_dict = {"column_default": "None"}
column_default_value_for_quotation_required_dict = {
    "column_default": "test_default_value"
}
column_default_value_for_quotation_not_required_dict = {"column_default": "9999"}

nullable_column_flag_no_dict = {"nullable_column_flag": "NO"}
nullable_column_flag_yes_dict = {"nullable_column_flag": "YES"}

column_value_quotation_not_required_dict = {"no_quotation": "○"}
column_value_quotation_required_dict = {"no_quotation": "None"}

test_case_1 = [
    (
        "data type unicode, with column default, nullable yes, add quotation to value, cell value 'None' string, set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | unicode_column_data_type_dict
            | column_default_value_for_quotation_required_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_required_dict,
            cell_value="None",
            set_empty_str_instead_of_null_value=True,
            expected="N'test_default_value'",
        ),
    ),
]

test_case_2 = [
    (
        "data type unicode, with column default, nullable no, add quotation to value, cell value None, set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | unicode_column_data_type_dict
            | column_default_value_for_quotation_required_dict
            | nullable_column_flag_no_dict
            | column_value_quotation_required_dict,
            cell_value=None,
            set_empty_str_instead_of_null_value=True,
            expected="N'test_default_value'",
        ),
    ),
]

test_case_3 = [
    (
        "data type unicode, with column default, nullable no, no quotation to value, cell value empty string, do not set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | unicode_column_data_type_dict
            | column_default_value_for_quotation_required_dict
            | nullable_column_flag_no_dict
            | column_value_quotation_not_required_dict,
            cell_value="",
            set_empty_str_instead_of_null_value=False,
            expected="test_default_value",
        ),
    ),
]

test_case_4 = [
    (
        "data type unicode, without column default, nullable yes, add quotation to value, cell value exists, do not set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | unicode_column_data_type_dict
            | column_default_no_value_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_required_dict,
            cell_value="test_cell_value",
            set_empty_str_instead_of_null_value=False,
            expected="N'test_cell_value'",
        ),
    ),
]

test_case_5 = [
    (
        "data type non-unicode, with column default, nullable no, no quotation to value, cell value 'None' string, do not set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | non_unicode_column_data_type_dict
            | column_default_value_for_quotation_required_dict
            | nullable_column_flag_no_dict
            | column_value_quotation_not_required_dict,
            cell_value="None",
            set_empty_str_instead_of_null_value=False,
            expected="test_default_value",
        ),
    ),
]

test_case_6 = [
    (
        "data type non-unicode, without column default, nullable yes, no quotation to value, cell value None, do not set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | non_unicode_column_data_type_dict
            | column_default_no_value_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_not_required_dict,
            cell_value=None,
            set_empty_str_instead_of_null_value=False,
            expected="null",
        ),
    ),
]

test_case_7 = [
    (
        "data type non-unicode, without column default, nullable yes, add quotation to value, cell value exists, set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | non_unicode_column_data_type_dict
            | column_default_no_value_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_required_dict,
            cell_value="test_cell_value",
            set_empty_str_instead_of_null_value=True,
            expected="'test_cell_value'",
        ),
    ),
]

test_case_8 = [
    (
        "data type non-unicode, without column default, nullable yes, add quotation to value, cell value empty string, set empty string instead of null",
        Item(
            db_column_dict=column_base_dict
            | non_unicode_column_data_type_dict
            | column_default_no_value_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_required_dict,
            cell_value="",
            set_empty_str_instead_of_null_value=True,
            expected="''",
        ),
    ),
]

test_case_9 = [
    (
        "data type no-quote, with column default, nullable yes, cell value None",
        Item(
            db_column_dict=column_base_dict
            | no_quote_column_data_type_dict
            | column_default_value_for_quotation_not_required_dict
            | nullable_column_flag_yes_dict
            | column_value_quotation_required_dict,
            cell_value=None,
            set_empty_str_instead_of_null_value=True,
            expected="9999",
        ),
    ),
]

test_case_10 = [
    (
        "data type no-quote, with column default, nullable no, cell value exists",
        Item(
            db_column_dict=column_base_dict
            | no_quote_column_data_type_dict
            | column_default_value_for_quotation_not_required_dict
            | nullable_column_flag_no_dict
            | column_value_quotation_required_dict,
            cell_value="1",
            set_empty_str_instead_of_null_value=True,
            expected="1",
        ),
    ),
]

test_case_11 = [
    (
        "data type no-quote, with column default, nullable no, cell value empty string",
        Item(
            db_column_dict=column_base_dict
            | no_quote_column_data_type_dict
            | column_default_value_for_quotation_not_required_dict
            | nullable_column_flag_no_dict
            | column_value_quotation_required_dict,
            cell_value="",
            set_empty_str_instead_of_null_value=True,
            expected="9999",
        ),
    ),
]

test_params = (
    test_case_1
    + test_case_2
    + test_case_3
    + test_case_4
    + test_case_5
    + test_case_6
    + test_case_7
    + test_case_8
    + test_case_9
    + test_case_10
    + test_case_11
)


class TestClass:
    @pytest.mark.parametrize(
        "no, description",
        [(index + 1, test_param[0]) for index, test_param in enumerate(test_params)],
    )
    def test_pattern(self, no: int, description: str):
        test_value = test_params[no - 1][1]

        a_request = DMLValueBuildRequest(
            db_column=DBColumnTestBuilder.from_dict(test_value.db_column_dict),
            cell_value=test_value.cell_value,
            set_empty_str_instead_of_null=SetEmptyStrInsteadOfNull(
                test_value.set_empty_str_instead_of_null_value
            ),
        )

        actual = DMLValueBuilder.execute(a_request=a_request)

        assert actual == test_value.expected