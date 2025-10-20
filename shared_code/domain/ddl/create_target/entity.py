from dataclasses import dataclass
from typing import Any

from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName
from shared_code.domain.table.table_name.set import TableNameSet


@dataclass(frozen=True)
class DDLCreateTarget:
    schema: Schema
    include_table_name_set: TableNameSet
    exclude_table_name_set: TableNameSet

    @classmethod
    def from_dict(cls, dict_obj: dict[str, Any]) -> "DDLCreateTarget":
        schema = Schema(value=dict_obj["schema"])
        include_table_name_set = TableNameSet.from_str_list(
            str_list=dict_obj.get("include_tables", [])
        )
        exclude_table_name_set = TableNameSet.from_str_list(
            str_list=dict_obj.get("exclude_tables", [])
        )

        return cls(
            schema=schema,
            include_table_name_set=include_table_name_set,
            exclude_table_name_set=exclude_table_name_set,
        )

    def is_target(self, table_name: TableName) -> bool:
        if self.include_table_name_set.is_empty():
            return True

        return self.include_table_name_set.contains(element=table_name)

    def is_not_target(self, table_name: TableName) -> bool:
        if not self.is_target(table_name=table_name):
            return True

        if self.exclude_table_name_set.is_empty():
            return False

        return self.exclude_table_name_set.contains(element=table_name)