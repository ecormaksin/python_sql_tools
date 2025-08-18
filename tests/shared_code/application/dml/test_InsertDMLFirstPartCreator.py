from shared_code.application.dml.insert_dml_first_part_creator import (
    InsertDMLFirstPartCreator,
    InsertDMLFirstPartCreationRequest,
)
from shared_code.domain.table_name import TableName
from tests.shared_code.application.db_column.list_test_builder import (
    DBColumnsTestBuilder,
)


class TestClass:
    def test_media_type(self):
        db_columns = DBColumnsTestBuilder.media_type()
        insert_dml_first_part = InsertDMLFirstPartCreator.execute(
            a_request=InsertDMLFirstPartCreationRequest(
                table_name=TableName(value="media_type"), db_columns=db_columns
            )
        )

        assert (
            insert_dml_first_part
            == "INSERT INTO media_type (media_type_id, name) VALUES ("
        )
