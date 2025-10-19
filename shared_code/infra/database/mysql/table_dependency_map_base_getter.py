from shared_code.domain.schema.entity import Schema
from shared_code.domain.table.table_name.entity import TableName
from shared_code.domain.table.table_type import TableType
from shared_code.domain.table_dependency.entity import TableDependency
from shared_code.domain.table_dependency.map import TableDependencyMap
from shared_code.domain.table_name_with_schema.entity import TableNameWithSchema
from shared_code.domain.table_name_with_schema.set import TableNameWithSchemaSet


class TableDependencyMapBaseGetter:
    @classmethod
    def execute(
        cls, cursor, table_dependency_map: TableDependencyMap, schema: Schema
    ) -> TableDependencyMap:
        query = """
        select 
          TABLE_NAME as table_name,
          TABLE_TYPE as table_type
        from 
          information_schema.TABLES
        where 
          TABLE_SCHEMA = %s
        """

        cursor.execute(query, (schema.value,))
        rows = cursor.fetchall()

        for row in rows:
            table_name = TableName(value=row["table_name"])
            table_name_with_schema = TableNameWithSchema(
                schema=schema, table_name=table_name
            )
            table_type = TableType.from_mysql_value(mysql_value=row["table_type"])

            table_dependency = TableDependency(
                table_name_with_schema=table_name_with_schema,
                table_type=table_type,
                dependent_table_set=TableNameWithSchemaSet.empty(),
            )

            table_dependency_map = table_dependency_map.put(
                table_name_with_schema, table_dependency
            )

        return table_dependency_map