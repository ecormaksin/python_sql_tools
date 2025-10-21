import re

from shared_code.domain.table.table_name.entity import TableName


class CreateViewStatementGetter:
    @classmethod
    def execute(cls, cursor, view_name: TableName) -> str:
        query = "show create view " + view_name.value

        cursor.execute(query)
        row = cursor.fetchone()

        raw_value = str(row["Create View"])

        replaced_value = raw_value
        replaced_value = re.sub(
            r"ALGORITHM=(UNDEFINED|MERGE|TEMPTABLE) ", "", replaced_value
        )
        replaced_value = re.sub(
            r"DEFINER=`[a-zA-Z0-9_]{1,32}`@`[a-zA-Z0-9_.%]{1,60}` ",
            "",
            replaced_value,
        )
        replaced_value = re.sub(r"SQL SECURITY (DEFINER|INVOKER) ", "", replaced_value)

        return replaced_value + ";"
