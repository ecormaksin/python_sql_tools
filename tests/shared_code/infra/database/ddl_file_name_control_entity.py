from typing import Optional
from dataclasses import dataclass

@dataclass
class DDLFileNameControlEntity:
    NUMBER_LENGTH = 2

    schema_name: str
    view: Optional[int] = None

    def get_file_name(self, serial_number: int) -> str:
        return str(serial_number).zfill(self.NUMBER_LENGTH) + "." + self.schema_name + ".sql"

    def get_view_file_name(self) -> str:
        if not self.view:
            raise RuntimeError("ビューのファイル名連番を指定してください。")

        return self.get_file_name(self.view)

@dataclass
class DDLFileNameControlEntityList:
    a_list = [
        DDLFileNameControlEntity(schema_name="artist"),
        DDLFileNameControlEntity(schema_name="genre"),
        DDLFileNameControlEntity(schema_name="media_type"),
        DDLFileNameControlEntity(schema_name="album", view=1),
        DDLFileNameControlEntity(schema_name="play_list"),
        DDLFileNameControlEntity(schema_name="employee"),
        DDLFileNameControlEntity(schema_name="customer"),
        DDLFileNameControlEntity(schema_name="invoice")
    ]

    @classmethod
    def get(cls) -> list[DDLFileNameControlEntity]:
        return DDLFileNameControlEntityList.a_list
