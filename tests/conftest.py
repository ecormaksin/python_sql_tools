import pytest


def pytest_addoption(parser):
    parser.addoption("--run-db2", action="store_true", default=False, help="Run tests marked as db2")

def pytest_runtest_setup(item):
    if "db2" in item.keywords and not item.config.getoption("--run-db2"):
        pytest.skip("""Use --run-db2 to run these tests. 
A DB2 instance is needed. 
Please specify the following environment variables:
    DB2_USER (default: db2inst1)
    DB2_PASSWORD (default: password)
    DB2_HOST (default: localhost)
    DB2_PORT (default: 50000)
    DB2_DBNAME (default: testdb)
""")
