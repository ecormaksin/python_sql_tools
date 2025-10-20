from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName
from shared_code.domain.table_dependency.map import TableDependencyMap
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema


class TableDependencyTableReferenceGetter:
    @classmethod
    def execute(
        cls, cursor, table_dependency_map: TableDependencyMap, schema: Schema
    ) -> TableDependencyMap:
        query = """
        select
          DISTINCT
          TABLE_NAME as table_name,
          REFERENCED_TABLE_SCHEMA as referenced_table_schema,
          REFERENCED_TABLE_NAME as referenced_table_name
        from
          information_schema.KEY_COLUMN_USAGE
        where
          TABLE_SCHEMA = %s
          and REFERENCED_TABLE_NAME is not null
        """

        cursor.execute(query, (schema.value,))
        rows = cursor.fetchall()

        for row in rows:
            table_name = TableName(value=row["table_name"])
            table_name_with_schema = TableNameWithSchema(
                schema=schema, table_name=table_name
            )

            dependent_table = TableNameWithSchema(
                schema=Schema(value=row["referenced_table_schema"]),
                table_name=TableName(value=row["referenced_table_name"]),
            )

            table_dependency = table_dependency_map.get(key=table_name_with_schema)
            assert table_dependency

            dependent_table_set = table_dependency.dependent_table_set
            dependent_table_set = dependent_table_set.put(element=dependent_table)
            new_table_dependency = table_dependency.update_dependent_table_set(
                dependent_table_set=dependent_table_set
            )

            table_dependency_map = table_dependency_map.put(
                key=table_name_with_schema, value=new_table_dependency
            )

        return table_dependency_map