# SQLツール用Pythonスクリプト

以下の機能をPythonのスクリプトで作成しています。

1. **【MySQLのみ対応】** 接続先のデータベースからDDLファイルを作成する。（`create_ddl` モジュール）

   - 複数データベース、テーブル指定／除外に対応しています。</br></br>

1. **【MySQLのみ対応】** 指定ビューを構成するテーブルの一覧をテキストファイルへ出力する。（`create_view_dependant_table_list` モジュール）</br></br>

1. **【MySQLのみ対応】** 接続先のデータベースからDMLの作成元となるxlsxファイルを作成する。（`create_dml_source_xlsx` モジュール）

    - [A5:SQL Mk-2](https://a5m2.mmatsubara.com/) のエンティティ定義CSVを出力する機能を参考にしました。</br></br>

1. xlsxファイルに設定したデータを元にINSERT文のDMLファイルを作成する。（`create_dml` モジュール）
     - 次のRDBMSに対応: MySQL, PostgreSQL, Oracle Database, SQL Server, Db2</br></br>

1. **【MySQLのみ対応】** 指定フォルダー配下のSQLファイルを再帰的に実行する。（`execute_sql` モジュール）</br></br>

1. **【MySQLのみ対応】** 接続先のデータベースから [DBUnit](https://dbunit.sourceforge.net/dbunit/) 用のFlatXMLファイルを出力する。（`export_dbunit_flatxml` モジュール）

     - [DBeaver](https://dbeaver.com/docs/dbeaver/Data-export/#dbunit) にもDBUnit用のFlatXMLをエクスポートする機能はありますが、複数テーブルを一括でエクスポートするにはデータベースナビゲータで対象のテーブルを全選択する必要があったり、カラムのデータ型がjsonの場合に引用符のエスケープが適切に行われないなどの使いづらさがありました。
     そのため、jsonカラムの引用符エスケープに対応した一括エクスポート機能を作成しました。</br></br>

## 1. 環境構築

### 1.1. 仮想環境の作成・ライブラリのインストール

ライブラリの管理に [Poetry](https://python-poetry.org/) を使っています。  
以下のコマンドを実行してください。

```sh, powershell
poetry config virtualenvs.in-project true
poetry install --no-root
```

- Windowsの場合

```powershell
.venv\Scripts\activate
```

- Linux, macOSの場合

```sh
.venv/Scripts/activate
```

### 1.2. 設定ファイルの準備

#### 1.2.1. 設定ファイルの種類と影響するモジュールの関係

| モジュール                  | 当スクリプト制御用設定ファイル | DB接続用設定ファイル |
|------------------------|:---------------:|:-----------:|
| create_ddl             | －               | ○           |
| create_dml_source_xlsx | ○               | ○           |
| create_dml             | ○               | －           |
| execute_sql            | －               | ○           |
| export_dbunit_flatxml  | －               | ○           |

#### 1.2.2. 当スクリプト制御用設定ファイル

- 各種コマンドの実行時に設定ファイルのパスを指定しない場合: `app_config-sample.json` を同じ階層に `app_config.json` としてコピー
- 各種コマンドの実行時に設定ファイルのパスを指定する場合: `app_config-sample.json`を任意のパスにコピー（ファイル名も別名に変更可）

当ファイルの設定内容については、別紙「[当スクリプト制御用設定ファイルの説明](./doc/app_config.md)」を参照してください。

#### 1.2.3. DB接続用設定ファイル

- 各種コマンドの実行時に設定ファイルのパスを指定しない場合: `db_config-sample.json` を同じ階層に `db_config.json` としてコピー
- 各種コマンドの実行時に設定ファイルのパスを指定する場合: `db_config-sample.json`を任意のパスにコピー（ファイル名も別名に変更可）

## 2. 各処理の実行

それぞれ別紙を参照してください。

- [指定ビューを構成するテーブルの一覧をテキストファイルへ出力する処理（`create_view_dependant_table_list` モジュール）](./doc/create_view_dependant_table_list.md)
- [接続先のデータベースからDDLファイルを作成する処理（`create_ddl` モジュール）](./doc/create_ddl.md)
- [接続先のデータベースからDMLの作成元となるxlsxファイルを作成する処理（`create_dml_source_xlsx` モジュール）](./doc/create_dml_source_xlsx.md)
- [xlsxファイルからDMLファイルを出力する処理（`create_dml`モジュール）](./doc/create_dml.md)
- [指定フォルダー配下のSQLファイルを再帰的に実行する処理（`execute_sql` モジュール）](./doc/execute_sql.md)
- [接続先のデータベースからDBUnit用のFlatXMLファイルを出力する処理（`export_dbunit_flatxml` モジュール）](./doc/export_dbunit_flatxml.md)

## サンプル ファイルの説明

`sample` フォルダ配下に、[DBeaver Community](https://dbeaver.io/) のサンプル データベース（H2）の各RDBMS向けER図、DMLファイル作成元xlsx、SQLファイルを格納しています。

- `sample/common/dbeaver_sample_db_data_with_domain_data_type_without_nvarchar.xlsx`
  - A5:SQL のドメインデータ型を使っているので、Db2・MySQL・PostgreSQLで使えます。