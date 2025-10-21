import re

from shared_code.domain.table.table_name.entity import TableName


class CreateTableStatementGetter:
    @classmethod
    def execute(cls, cursor, table_name: TableName) -> list[str]:
        table_name_value = table_name.value
        query = f"show create table {table_name_value}"

        cursor.execute(query)
        row = cursor.fetchone()

        raw_value = str(row["Create Table"])

        replaced_value = raw_value
        replaced_value = re.sub(r".*\s+FOREIGN\s+KEY\s+.*\r?\n", "", replaced_value)
        replaced_value = re.sub(
            r"ENGINE=[a-zA-Z0-9]+\s+DEFAULT\s+CHARSET=[a-zA-Z0-9_]+\s+COLLATE=[a-zA-Z0-9_]+",
            "",
            replaced_value,
        )
        replaced_value += ";"

        statements = replaced_value.split("\n")

        statements = cls.__remove_last_part_invalid_comma(statements=list(statements))

        return statements

    @classmethod
    def __remove_last_part_invalid_comma(cls, statements: list[str]) -> list[str]:
        # ステートメント全体の閉じカッコの前が "," になっていた場合は文法エラーになるので除去する
        for index, line in enumerate(reversed(statements)):
            matched = re.match(r"^\)", line)

            if matched:
                previous_line_index = (len(statements) - 1) - index - 1
                previous_line = statements[previous_line_index]
                previous_line = re.sub(r",$", "", previous_line)
                statements[previous_line_index] = previous_line
                break

        return statements