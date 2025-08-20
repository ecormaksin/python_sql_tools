from typing import Optional

from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.no_quotation import NoQuotation


class ValueQuotationGetter:
    @classmethod
    def execute(cls, data_type: DataType, no_quotation: Optional[NoQuotation]) -> str:
        if no_quotation:
            return ""
        return "'" if data_type.do_add_quotation() else ""
