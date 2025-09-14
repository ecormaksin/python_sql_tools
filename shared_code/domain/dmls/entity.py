from dataclasses import dataclass

from shared_code.domain.table_name import TableName


@dataclass(frozen=True)
class OneTableDmls:
    table_name: TableName
    dmls: list[str]

    @property
    def number_of_lines(self) -> int:
        return len(self.dmls)
