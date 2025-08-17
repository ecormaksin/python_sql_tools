import traceback

from openpyxl import load_workbook

from shared_code.application.dml_creator import DMLCreator
from shared_code.domain.app_config import AppConfig
from shared_code.domain.table_name import TableName
from shared_code.domain.table_name_definition_type import TableNameDefinitionType
from shared_code.infra.file_system.directory_creator import DirectoryCreator
from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class DMLFilesCreator:
    def __init__(
        self, src_xlsx_file_path: str, sink_dml_dir_path: str, app_config: AppConfig
    ):
        self.__src_xlsx_file_path = src_xlsx_file_path
        self.__sink_dml_dir_path = sink_dml_dir_path
        self.__app_config = app_config

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self):
        src_excel_file_path = self.__src_xlsx_file_path
        sink_dml_dir_path = self.__sink_dml_dir_path
        app_config = self.__app_config

        if FileExistenceChecker.not_exists(file_path=self.__src_xlsx_file_path):
            raise RuntimeError(f"source file '{src_excel_file_path}' not found.")

        try:
            DirectoryCreator.execute(path_str=sink_dml_dir_path)
        except Exception:
            stacktrace_str = traceback.format_exc()
            raise RuntimeError(
                f"cannot create dml output directory '{sink_dml_dir_path}'. detail: {stacktrace_str}"
            )

        a_workbook = load_workbook(
            filename=src_excel_file_path, data_only=True, read_only=True
        )

        sheet_name = "track"
        a_worksheet = a_workbook[sheet_name]

        if app_config.table_name_definition_type == TableNameDefinitionType.SHEET:
            table_name = TableName(value=sheet_name)

        with DMLCreator(
            table_name=table_name, a_worksheet=a_worksheet, app_config=app_config
        ) as a_dml_creator:
            dmls = a_dml_creator.execute()

        # for sheet_name in a_workbook.sheetnames:
        #     a_worksheet = a_workbook[sheet_name]
        #
        #     if app_config.table_name_definition_type == TableNameDefinitionType.SHEET:
        #         table_name = TableName(value=sheet_name)
        #
        #     print("")
        #     print("---")
        #     print(sheet_name)
        #     print("min_row: " + str(a_worksheet.min_row))
        #     print("max_row: " + str(a_worksheet.max_row))
        #     print("min_column: " + str(a_worksheet.min_column))
        #     print("max_column: " + str(a_worksheet.max_column))
