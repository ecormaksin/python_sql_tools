from dataclasses import dataclass

from shared_code.domain.db_column.column_comment import ColumnComment
from shared_code.domain.db_column.column_default import ColumnDefault
from shared_code.domain.db_column.column_name import ColumnName
from shared_code.domain.db_column.data_type import DataType
from shared_code.domain.db_column.entity import DBColumn
from shared_code.domain.db_column.key_position import KeyPosition
from shared_code.domain.db_column.list import DBColumns
from shared_code.domain.db_column.nullable_column_flag import NullableColumnFlag
from shared_code.domain.entity_definition.entity import EntityDefinition
from shared_code.domain.entity_definition.map import EntityDefinitions
from shared_code.domain.table.table_name.entity import TableName
from shared_code.domain.table.table_name.set import TableNameSet
from shared_code.infra.database.mysql.connector import MySQLConnector


@dataclass(frozen=True)
class EntityDefinitionsGetRequest:
    db_config_json_file_path_str: str
    target_table_name_set: TableNameSet


@dataclass(frozen=True)
class EntityDefinitionsGetResponse:
    table_name_set: TableNameSet
    entity_definitions: EntityDefinitions


class EntityDefinitionsGetter:
    @classmethod
    def execute(
        cls, a_request: EntityDefinitionsGetRequest
    ) -> EntityDefinitionsGetResponse:
        target_table_name_set = a_request.target_table_name_set

        actual_table_name_set = TableNameSet.empty()
        entity_definitions = EntityDefinitions.empty()

        with MySQLConnector(
            config_json_file_path_str=a_request.db_config_json_file_path_str
        ) as db_connector:
            db_connection = db_connector.connect()
            with db_connection.cursor(buffered=True, dictionary=True) as cur:
                query = """
                select
                    sq_a.table_name as table_name,
                    sq_a.column_name as column_name,
                    sq_a.column_comment as column_comment,
                    sq_a.column_default as column_default,
                    sq_a.is_nullable as is_nullable,
                    sq_a.column_type as column_type,
                    case 
                        when sq_b.ORDINAL_POSITION is null then ''
                        else sq_b.ORDINAL_POSITION
                    end as key_position
                from
                    information_schema.`COLUMNS` sq_a
                    left outer join information_schema.KEY_COLUMN_USAGE sq_b
                        on 
                        sq_b.TABLE_SCHEMA = sq_a.TABLE_SCHEMA 
                        and sq_b.TABLE_NAME = sq_a.TABLE_NAME 
                        and sq_b.CONSTRAINT_NAME = 'PRIMARY'
                        and sq_b.column_name = sq_a.column_name
                    inner join information_schema.TABLES sq_c
                        on
                        sq_c.TABLE_SCHEMA = sq_a.TABLE_SCHEMA
                        and sq_c.TABLE_NAME = sq_a.TABLE_NAME 
                        and sq_c.TABLE_TYPE = 'BASE TABLE'
                where
                    sq_a.TABLE_SCHEMA = %s {TARGET_TABLE_CLAUSE}
                order by
                    sq_a.table_name,
                    sq_a.ORDINAL_POSITION
                """

                if target_table_name_set.is_empty():
                    query = query.replace("{TARGET_TABLE_CLAUSE}", "")
                else:
                    query = query.replace(
                        "{TARGET_TABLE_CLAUSE}",
                        "and sq_a.table_name in ("
                        + target_table_name_set.in_clause()
                        + ")",
                    )

                cur.execute(query, (db_connector.database_name,))
                rows = cur.fetchall()

                for row in rows:
                    table_name = TableName(value=row["table_name"])
                    actual_table_name_set = actual_table_name_set.put(
                        element=table_name
                    )

                    if entity_definitions.not_contains(key=table_name):
                        entity_definitions = entity_definitions.put(
                            key=table_name,
                            value=EntityDefinition(
                                table_name=table_name, db_columns=DBColumns.empty()
                            ),
                        )

                    entity_definition = entity_definitions.get(key=table_name)

                    db_columns = entity_definition.db_columns

                    column_comment = row["column_comment"]
                    column_default = row["column_default"]
                    key_position = row["key_position"]

                    db_columns = db_columns.append(
                        element=DBColumn(
                            column_name=ColumnName(value=row["column_name"]),
                            column_comment=ColumnComment(value=column_comment)
                            if column_comment
                            else None,
                            column_default=ColumnDefault(value=column_default)
                            if column_default
                            else None,
                            nullable_column_flag=NullableColumnFlag.from_str(
                                key=row["is_nullable"]
                            ),
                            data_type=DataType(value=row["column_type"]),
                            key_position=KeyPosition(value=int(key_position))
                            if key_position
                            else None,
                            no_quotation=None,
                        )
                    )

                    entity_definitions = entity_definitions.put(
                        key=table_name,
                        value=EntityDefinition(
                            table_name=table_name, db_columns=db_columns
                        ),
                    )

        return EntityDefinitionsGetResponse(table_name_set=actual_table_name_set, entity_definitions=entity_definitions)