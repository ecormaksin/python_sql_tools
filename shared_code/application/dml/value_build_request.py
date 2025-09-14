from dataclasses import dataclass
from typing import Optional

from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.set_empty_str_instead_of_null import SetEmptyStrInsteadOfNull


@dataclass(frozen=True)
class DMLValueBuildRequest:
    db_column: DBColumn
    cell_value: Optional[str]
    set_empty_str_instead_of_null: SetEmptyStrInsteadOfNull
