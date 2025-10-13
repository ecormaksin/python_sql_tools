# xlsxファイルからDMLファイルを出力する処理(`create_dml`モジュール)

## 実行手順

### 1. 各種ファイルの準備

- 設定ファイル（「[当スクリプト制御用設定ファイル](../README.md#122-当スクリプト制御用設定ファイル)」）</br></br>

- DML作成元xlsxファイル
  - 投入データ設定用テンプレートの準備
    - MySQLの場合は [create_dml_source_xlsxモジュール](./create_dml_source_xlsx.md) からデータ設定用のファイルを作成可能です。</br></br>

    - その他のRDBMSについては、[A5:SQL Mk-2のエンティティ定義CSV出力](https://a5m2.mmatsubara.com/help/TableEditor/tableDefine.html) で出力される `a5m2_COLUMNS.csv` などを元にカラム情報を取得してください。
      `TABLE_NAME` 単位で `COLUMN_NAME` ～ `KEY_POSITION` までの情報を使いますが、 `ORDINAL_POSITION` は除外してください。</br></br>

    - シート名に制約はありません。ただし、Excel自体の制約として31文字以内です。</br></br>

    - DMLはシートの順番にファイル名に連番を付加して出力されます。
      外部キー制約がある場合はシートの順序に注意してください。</br></br>

      - テーブルの依存関係を確認する方法の例として、[A5:SQL Mk-2](https://a5m2.mmatsubara.com/) のER図から生成されたDDLファイルを使う方法を記載します。
         1. DDLの生成時に「`テーブル生成順序`: 依存関係順（依存する方が先）」を指定します。
         2. 以下のコマンドを実行します。
              - Bashの場合

                 ```bash
                 CREATE_TABLES_DDL="<DDLファイルのパス>"
                 grep -oP 'CREATE TABLE\s+\K[^\s(]+' $CREATE_TABLES_DDL
                 ```

              - PowerShellの場合

                 ```pwsh
                 $createTablesDDL = "<DDLファイルのパス>"
                 Get-Content -Path $createTablesDDL | Where-Object { $_ -match "CREATE TABLE " } | ForEach-Object { $tableName = $_ -replace "CREATE TABLE "; $tableName = $tableName -replace " \(", ""; Write-Host $tableName; }
                 ```

         3. 依存しているテーブル名から出力されるので、逆順でシートを調整します。</br></br>

  - 投入用データの設定
    - 当スクリプト制御用設定ファイルの `data_start_cell.row`, `data_start_cell.column` がデータの開始位置となります。（`app_config-sample.json` では セルD8（R8C4））</br></br>

    - 行＝データベースのレコードとなります。</br></br>

    - カラム情報の終端列から空列を1つ設け、それ以降に元となるデータを設定し、Excelの数式を使って投入データを設定できます。
      （例: 日時データを領域外に入力しておき、投入用データ部分では `=TEXT(<元データのセル>, "yyyy-mm-dd hh:mm:ss")` でフォーマットを指定して文字列化する。）</br></br>

    - 通常INSERT文で値に引用符が付加されるカラムに、データベースの関数を使って値を設定したい場合は、当スクリプト制御用設定ファイルの `no_quotation_row` で指定した行番号の該当カラムに"○"などの値を入力してください。
      引用符が付加されなくなります。
      1シート内で同じカラムに対し引用符を付加する／しないを制御することはできません。
      同じテーブルへの投入データであってもシートを分けて対応してください。

### 2. コマンドの実行

`python -m create_dml --help` で実行時のパラメーターを確認できます。

以下は日本語で表にまとめたものです。

| ショート | ロング           | 必須 | 説明                                                                                                                           |
|------|---------------|:--:|------------------------------------------------------------------------------------------------------------------------------|
| -s   | --source      | ○  | DMLファイル作成元のxlsxファイルのパスを指定します。                                                                                                |
| -d   | --destination | －  | DMLファイルの出力先フォルダーのパスを指定します。<br/>未指定の場合は一時フォルダ（`tempfile.gettempdir()`）の`python_sql_tools/dml/<実行日時(%Y%m%d-%H%M%S-%f)>`に出力します。 |
| -c   | --config      | －  | 当スクリプト制御用設定ファイル（.json）のパスを指定します。<br/>未指定の場合、プロジェクト ルートの 'app_config.json' を検索します。                                            |
