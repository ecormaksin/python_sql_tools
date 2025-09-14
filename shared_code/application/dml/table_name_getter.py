from dataclasses import dataclass

from openpyxl.worksheet.worksheet import Worksheet

from shared_code.domain.cell_position import CellPosition
from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class TableNameGetRequest:
    a_worksheet: Worksheet
    table_name_cell_position: CellPosition


class TableNameGetter:
    @classmethod
    def execute(cls, a_request: TableNameGetRequest) -> TableName:
        a_worksheet = a_request.a_worksheet
        table_name_cell_position = a_request.table_name_cell_position

        a_cell = a_worksheet.cell(
            row=table_name_cell_position.row,
            column=table_name_cell_position.column,
        )
        table_name = TableName(value=str(a_cell.value))

        return table_name
