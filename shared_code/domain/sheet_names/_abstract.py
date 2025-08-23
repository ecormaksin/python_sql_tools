from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class SheetNames(ABC):
    value: str

    def do_have_value(self) -> bool:
        return True if self.value else False

    def contains(self, sheet_name: str) -> bool:
        index = self.value.find(sheet_name + ",")
        return False if index == -1 else True
