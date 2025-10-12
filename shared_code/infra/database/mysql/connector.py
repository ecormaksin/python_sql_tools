import json

import mysql.connector


class MySQLConnector:
    def __init__(self, config_json_file_path_str: str):
        with open(config_json_file_path_str, "r", encoding="utf-8") as file_obj:
            self.__config = json.load(file_obj)

        self.__connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    @property
    def database_name(self) -> str:
        return self.__config["database"]

    def connect(self):
        if self.__connection:
            return self.__connection

        config = self.__config
        self.__connection = mysql.connector.connect(**config)

        return self.__connection
