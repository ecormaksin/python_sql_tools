# SQLツール用Pythonスクリプト

- 1つのxlsxファイル内にDBテーブルごとのシートを設けることで、対象シート（テーブル）のすべてのINSERT文のファイルを出力します。

## 1. 環境構築

ライブラリの管理に [Pipenv](https://pipenv.pypa.io/en/latest/) を使っています。  
以下のコマンドでライブラリをインストールしてください。

```sh
pipenv sync
```

## 2. xlsxファイルからDMLファイルを出力する処理(`create_dml`モジュール)

### 2.1. 各種ファイルの準備

1. 設定ファイル（`*.json`）を準備します。（`app_config-sample.json` をコピーして使ってください。）
   - 設定ファイルのパスを指定しない場合
     - プロジェクト フォルダーの直下に `app_config.json` を配置します。
   - 設定ファイルのパスを指定する場合
     - 任意の場所へjsonファイルを任意の名前で配置します。</br></br>

1. DMLファイルの作成元となるxlsxファイルを任意のパスへ作成します。  
  テンプレートは `sample` フォルダー内の `dbeaver_sample_db*_data*.xlsx` をコピーして使ってください。  
  シート順に連番を先頭に付加してDMLファイル名を生成しています。  
  テーブル間の外部キーの依存関係に留意してシート順を調整してください。

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

1. 必要に応じて設定ファイルの内容を以下のように変更します。

#### 2.1.1 設定ファイルの変更

##### 2.1.1.1. xlsxファイルの行番号やセル位置と合わせる必要があるプロパティ

| プロパティ名                                    | 説明                             |
|-------------------------------------------|--------------------------------|
| table_name_cell.row, table_name_cell.cell | テーブル名のセル位置                     |
| column_name_row                           | カラム名の行番号                       |
| column_default_row                        | カラムのデフォルト値の行番号                 |
| nullable_column_flag_row                  | カラム値の必須／任意の行番号                 |
| data_type_row                             | データ型の行番号                       |
| key_position_row                          | 主キーのカラム順序の行番号（2025-09-11現在未使用） |
| no_quotation_row                          | 引用符を付加しないカラムを指定する行番号           |
| data_start_cell.row, data_start_cell.cell | データ開始のセル位置                     |

##### 2.1.1.2. DMLファイルの出力に影響のあるプロパティ

| プロパティ名                   | 説明                                                                                                                                                     |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| target_sheet_names       | 対象のシート名をカンマ区切りで指定します。<br/>DMLファイルを作成したいシートの方が少ない場合に使います。<br/>未指定（""）の場合は全シートが対象になります。<br/>exclude_sheet_namesに同じシート名が含まれている場合はエラーになります。                |
| exclude_sheet_names      | DMLファイルの作成を除外したいシート名をカンマ区切りで指定します。<br/>target_sheet_namesに同じシート名が含まれている場合はエラーになります。                                                                    |
| file_name_prefix         | DMLファイル名の先頭に共通で付加する文字列を指定します。<br/>例えば、あるフォルダ内にあらかじめ「01_truncate_tables.sql」のようなSQLファイルを配置していて、同じフォルダにDMLファイルを出力した時にファイル名の昇順で並び変えた時に実行順序通りにしたい時などに使います。 |
| number_of_lines_per_file | DMLファイル内の行数を指定します。<br/>-1の場合はシート内全件のステートメントが1ファイル内に出力されます。<br/>大量レコードのDMLを実行する時に、行数を分割してDMLファイルを出力したい場合に使います。                                          |

### 2.2. コマンドの実行

#### 2.2.1. 設定ファイルのパスを指定しない場合

```sh
python -m create_dml -s "<DML作成元xlsxファイルのパス>" -d "<DMLファイル作成先フォルダのパス>"
```

#### 2.2.2. 設定ファイルのパスを指定する場合

```sh
python -m create_dml -s "<DML作成元xlsxファイルのパス>" -d "<DMLファイル作成先フォルダのパス>" -c "設定ファイルのパス"
```

#### 2.2.3. 補足

`-d` オプションを指定しない場合、一時フォルダ（「`tempfile.gettempdir()` のOS依存結果」＋「`python-sql-tools/dml`」）に実行日時のフォルダ（`yyyyMMdd-HHmmss`）が作成され、その配下にDMLファイルが出力されます。

## サンプル ファイルの説明

`sample` フォルダ配下に、[DBeaver Community](https://dbeaver.io/) のサンプル データベース（H2）の各RDBMS向けER図、DMLファイル作成元xlsx、SQLファイルを格納しています。

- `sample/common/dbeaver_sample_db_data_with_domain_data_type_without_nvarchar.xlsx`
  - A5:SQL のドメインデータ型を使っているので、Db2・MySQL・PostgreSQLで使えます。