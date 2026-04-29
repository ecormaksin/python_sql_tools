import re

class SQLSplitter:
    @classmethod
    def execute(cls, source: str, separator: str = ";") -> list[str]:
        lines = re.split(r"\r?\n", source, flags=re.MULTILINE)

        blank_line_removed_lines = [line for line in lines if re.sub(r"^[ \t　]*$", "", line)]

        blank_line_removed_file_content = "\n".join(blank_line_removed_lines)

        escaped_separator = re.escape(separator)
        pattern = fr" *{escaped_separator} *$"
        ddl_list = re.split(pattern, blank_line_removed_file_content, flags=re.MULTILINE)

        return [ddl for ddl in ddl_list if ddl]
