import json5

from shared_code.domain.ddl.create_target.map import DDLCreateTargetMap


class DBConfigJsoncFileReader:
    @classmethod
    def get_ddl_create_target_map(
        cls, db_config_file_path_str: str
    ) -> DDLCreateTargetMap:
        with open(db_config_file_path_str, "r", encoding="utf-8") as file_obj:
            dict_obj = json5.load(file_obj)

        ddl_targets = dict_obj.get("ddl_target", [{"schema": dict_obj["database"]}])
        ddl_create_target_map = DDLCreateTargetMap.from_dict_list(dict_list=ddl_targets)

        return ddl_create_target_map
