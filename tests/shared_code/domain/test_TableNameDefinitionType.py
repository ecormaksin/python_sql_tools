from shared_code.domain.table_name_definition_type import TableNameDefinitionType


class TestClass:
    def test(self):
        assert TableNameDefinitionType.SHEET is TableNameDefinitionType.of("sheet")
