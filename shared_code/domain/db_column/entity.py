from dataclasses import dataclass
from typing import Optional

from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.no_quotation import NoQuotation


@dataclass(frozen=True)
class DBColumn:
    column_name: ColumnName
    data_type: DataType
    key_position: Optional[KeyPosition]
    no_quotation: Optional[NoQuotation]

    def __eq__(self, other):
        if not isinstance(other, DBColumn):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        column_name = repr(self.column_name)
        data_type = repr(self.data_type)
        key_position = repr(self.key_position) if self.key_position else "None"
        no_quotation = repr(self.no_quotation) if self.no_quotation else "None"
        return (
            "DBColumn("
            f"column_name={column_name}, "
            f"data_type={data_type}, "
            f"key_position={key_position}, "
            f"no_quotation={no_quotation}"
            ")"
        )
