from dataclasses import dataclass
from typing import Optional

from shared_code.domain.cell_position import CellPosition
from shared_code.domain.row_number import RowNumber
from shared_code.domain.table_name_definition_type import TableNameDefinitionType


@dataclass(frozen=True)
class AppConfig:
    table_name_definition_type: TableNameDefinitionType
    table_name_cell_position: Optional[CellPosition]
    db_column_name_row_number: RowNumber
    data_type_row_number: RowNumber
    data_start_cell_position: CellPosition
