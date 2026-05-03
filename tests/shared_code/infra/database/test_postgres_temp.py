from shared_code.infra.database.rdbms_type import RDBMSType
from tests.shared_code.infra.database.db_container_for_test import DbContainerForTest


class TestClass:
    def test(self):
        rdbms_type = RDBMSType.POSTGRES

        with DbContainerForTest(rdbms_type=rdbms_type) as test_container:
            print("test")
