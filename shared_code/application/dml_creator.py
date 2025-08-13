from shared_code.infra.file_system.file_existence_checker import FileExistenceChecker


class DMLCreator:
    def __init__(self, src_excel_file_path: str, sink_dml_folder_path: str):
        self.__src_excel_file_path = src_excel_file_path
        self.__sink_dml_folder_path = sink_dml_folder_path

    def __enter__(self):
        """
        do nothing
        """

    def __exit__(self, exc_type, exc_value, traceback):
        """
        do nothing
        """

    def execute(self):
        src_excel_file_path = self.__src_excel_file_path

        if FileExistenceChecker.not_exists(file_path=self.__src_excel_file_path):
            raise RuntimeError(f"「{src_excel_file_path}」が見つかりません。")
