from dataclasses import dataclass

from openpyxl.worksheet.worksheet import Worksheet


@dataclass(frozen=True)
class DBColumnsDataRangeGetRequest:
    a_worksheet: Worksheet
    max_row: int
    min_col: int


class DBColumnsDataRangeGetter:
    @classmethod
    def execute(cls, a_request: DBColumnsDataRangeGetRequest) -> list[list[str]]:
        return [
            [str(cell) for cell in col]
            for col in a_request.a_worksheet.iter_cols(
                min_row=1,
                max_row=a_request.max_row,
                min_col=a_request.min_col,
                values_only=True,
            )
        ]
