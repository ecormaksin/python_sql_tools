from dataclasses import dataclass
from typing import Any

from shared_code.domain.ddl.create_target.entity import DDLCreateTarget


@dataclass(frozen=True)
class DDLCreateTargetList:
    elements: list[DDLCreateTarget]

    @classmethod
    def from_dict_list(cls, dict_list: list[dict[str, Any]]) -> "DDLCreateTargetList":
        elements = []
        for a_dict in dict_list:
            element = DDLCreateTarget.from_dict(dict_obj=a_dict)
            elements.append(element)

        return cls(elements=elements)

    @classmethod
    def empty(cls) -> "DDLCreateTargetList":
        return cls(elements=list())

    def append(self, element: DDLCreateTarget) -> "DDLCreateTargetList":
        copied = list(self.elements)
        copied.append(element)
        return self.__class__(elements=copied)

    @property
    def unmodifiable_elements(self) -> list[DDLCreateTarget]:
        return list(self.elements)
