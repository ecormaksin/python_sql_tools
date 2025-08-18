from tests.shared_code.application.db_column.list_test_builder import (
    DBColumnsTestBuilder,
)


class TestClass:
    def test_list_build(self):
        db_columns = DBColumnsTestBuilder.media_type()

        assert db_columns
        assert len(db_columns.unmodifiable_elements) == 2
