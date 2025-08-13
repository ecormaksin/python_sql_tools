import sys

from shared_code.application.dml_creator import DMLCreator


def create_dml():
    if len(sys.argv) != 3:
        script = sys.argv[0]
        print(
            f"<DML作成元のExcelファイル パス> <DMLファイル出力先 フォルダー パス> を指定してください。"
        )
        sys.exit(1)

    src_excel_file_path = sys.argv[1]
    sink_dml_folder_path = sys.argv[2]

    with DMLCreator(
        src_excel_file_path=src_excel_file_path,
        sink_dml_folder_path=sink_dml_folder_path,
    ) as a_dml_creator:
        a_dml_creator.execute()


if __name__ == "__main__":
    create_dml()
