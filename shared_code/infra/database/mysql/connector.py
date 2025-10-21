import json

import mysql.connector

from shared_code.domain.schema.entity import Schema


class MySQLConnector:
    def __init__(self, config_json_file_path_str: str):
        with open(config_json_file_path_str, "r", encoding="utf-8") as file_obj:
            file_dict = json.load(file_obj)
            config_dict = {}
            for key in ["host", "user", "password", "port", "database"]:
                config_dict[key] = file_dict[key]
            self.__config = config_dict

        self.__connection = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def override_database(self, schema: Schema):
        self.__config["database"] = schema.value
        return self

    @property
    def database_name(self) -> str:
        return self.__config["database"]

    def connect(self):
        if self.__connection:
            return self.__connection

        config = self.__config
        self.__connection = mysql.connector.connect(**config)

        return self.__connection
