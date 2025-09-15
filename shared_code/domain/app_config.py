from dataclasses import dataclass
from typing import Optional

from shared_code.domain.cell_position import CellPosition
from shared_code.domain.file_name_prefix import FileNamePrefix
from shared_code.domain.number_of_lines_per_file import NumberOfLinesPerFile
from shared_code.domain.row_number import RowNumber
from shared_code.domain.set_empty_str_instead_of_null import SetEmptyStrInsteadOfNull
from shared_code.domain.sheet_names.exclude import ExcludeSheetNames
from shared_code.domain.sheet_names.target import TargetSheetNames


@dataclass(frozen=True)
class AppConfig:
    target_sheet_names: TargetSheetNames
    exclude_sheet_names: ExcludeSheetNames
    table_name_cell_position: CellPosition
    db_column_name_row_number: RowNumber
    column_default_row_number: RowNumber
    nullable_column_flag_row_number: RowNumber
    data_type_row_number: RowNumber
    key_position_row_number: RowNumber
    no_quotation_row_number: RowNumber
    data_start_cell_position: CellPosition
    set_empty_str_instead_of_null: SetEmptyStrInsteadOfNull
    file_name_prefix: Optional[FileNamePrefix]
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
        table_name_cell_position = repr(self.table_name_cell_position)
        column_name_row = repr(self.db_column_name_row_number)
        column_default_row = repr(self.column_default_row_number)
        nullable_column_flag_row = repr(self.nullable_column_flag_row_number)
        data_type_row = repr(self.data_type_row_number)
        key_position_row = repr(self.key_position_row_number)
        no_quotation_row = repr(self.no_quotation_row_number)
        data_start_cell = repr(self.data_start_cell_position)
        set_empty_str_instead_of_null = repr(self.set_empty_str_instead_of_null)
        file_name_prefix = (
            repr(self.file_name_prefix) if self.file_name_prefix else "None"
        )
        number_of_lines_per_file = repr(self.number_of_lines_per_file)

        return (
            "AppConfig("
            f"target_sheet_names={target_sheet_names}, "
            f"exclude_sheet_names={exclude_sheet_names}, "
            f"table_name_cell_position={table_name_cell_position}, "
            f"db_column_name_row_number={column_name_row}, "
            f"column_default_row_number={column_default_row}, "
            f"nullable_column_flag_row_number={nullable_column_flag_row}, "
            f"data_type_row_number={data_type_row}, "
            f"key_position_row_number={key_position_row}, "
            f"no_quotation_row_number={no_quotation_row}, "
            f"data_start_cell_position={data_start_cell}, "
            f"set_empty_str_instead_of_null={set_empty_str_instead_of_null}, "
            f"file_name_prefix={file_name_prefix}, "
            f"number_of_lines_per_file={number_of_lines_per_file}"
            ")"
        )

    @property
    def header_max_row(self) -> int:
        header_rows = [
            self.db_column_name_row_number.value,
            self.column_default_row_number.value,
            self.nullable_column_flag_row_number.value,
            self.data_type_row_number.value,
            self.key_position_row_number.value,
            self.no_quotation_row_number.value,
        ]
        return max(header_rows)
