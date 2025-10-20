from dataclasses import dataclass
from typing import Any

from shared_code.domain.ddl.create_target.entity import DDLCreateTarget
from shared_code.domain.schema.entity import Schema


@dataclass(frozen=True)
class DDLCreateTargetMap:
    elements: dict[Schema, DDLCreateTarget]

    @classmethod
    def from_dict_list(cls, dict_list: list[dict[str, Any]]) -> "DDLCreateTargetMap":
        elements = {}
        for a_dict in dict_list:
            element = DDLCreateTarget.from_dict(dict_obj=a_dict)
            elements[element.schema] = element

        return cls(elements=elements)

    @classmethod
    def empty(cls) -> "DDLCreateTargetMap":
        return cls(elements=dict())

    def put(self, key: Schema, element: DDLCreateTarget) -> "DDLCreateTargetMap":
        copied = dict(self.elements)
        copied[key] = element
        return self.__class__(elements=copied)

    def get(self, key: Schema) -> DDLCreateTarget:
        return self.elements[key]

    @property
    def unmodifiable_elements(self) -> dict[Schema, DDLCreateTarget]:
        return dict(self.elements)
