from dataclasses import dataclass
from typing import Optional

from shared_code.domain.cell_position import CellPosition
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.row_number import RowNumber
from shared_code.domain.sheet_names.exclude import ExcludeSheetNames
from shared_code.domain.sheet_names.target import TargetSheetNames


@dataclass(frozen=True)
class AppConfig:
    target_sheet_names: TargetSheetNames
    exclude_sheet_names: ExcludeSheetNames
    table_name_cell_position: Optional[CellPosition]
    db_column_name_row_number: RowNumber
    data_type_row_number: RowNumber
    key_position_row_number: Optional[RowNumber]
    no_quotation_row_number: Optional[RowNumber]
    data_start_cell_position: CellPosition
    number_of_lines_per_file: NumberOfLinesPerFile = NumberOfLinesPerFile.UNLIMITED

    def __eq__(self, other):
        if not isinstance(other, AppConfig):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        target_sheet_names = repr(self.target_sheet_names)
        exclude_sheet_names = repr(self.exclude_sheet_names)
        table_name_cell_position = (
            repr(self.table_name_cell_position)
            if self.table_name_cell_position
            else "None"
        )
        column_name_row = repr(self.db_column_name_row_number)
        data_type_row = repr(self.data_type_row_number)
        data_start_cell = repr(self.data_start_cell_position)
        number_of_lines_per_file = repr(self.number_of_lines_per_file)

        return (
            "AppConfig("
            f"target_sheet_names={target_sheet_names}, "
            f"exclude_sheet_names={exclude_sheet_names}, "
            f"table_name_cell_position={table_name_cell_position}, "
            f"db_column_name_row_number={column_name_row}, "
            f"data_type_row_number={data_type_row}, "
            f"data_start_cell_position={data_start_cell}, "
            f"number_of_lines_per_file={number_of_lines_per_file}"
            ")"
        )

    @property
    def header_max_row(self) -> int:
        key_position_row_number = self.key_position_row_number
        no_quotation_row_number = self.no_quotation_row_number
        header_rows = [
            self.db_column_name_row_number.value,
            self.data_type_row_number.value,
            self.key_position_row_number.value
            if key_position_row_number
            else RowNumber.UNDEFINED,
            no_quotation_row_number.value
            if no_quotation_row_number
            else RowNumber.UNDEFINED,
        ]
        return max(header_rows)
