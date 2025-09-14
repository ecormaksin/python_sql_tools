from dataclasses import dataclass

from openpyxl.worksheet.worksheet import Worksheet

from shared_code.domain.cell_position import CellPosition


@dataclass(frozen=True)
class DMLDataRangeGetRequest:
    a_worksheet: Worksheet
    data_start_cell_position: CellPosition


class DMLDataRangeGetter:
    @classmethod
    def execute(cls, a_request: DMLDataRangeGetRequest) -> list[list[str]]:
        a_worksheet = a_request.a_worksheet
        data_start_cell_position = a_request.data_start_cell_position

        return [
            [str(cell) for cell in row]
            for row in a_worksheet.iter_rows(
                min_row=data_start_cell_position.row,
                max_row=a_worksheet.max_row,
                min_col=data_start_cell_position.column,
                values_only=True,
            )
        ]
