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

    def overlapped(self, other: "SheetNames") -> bool:
        if not self.value or not other.value:
            return False

        self_list = self.value.split(",")
        other_list = other.value.split(",")

        common_sheet_names = set(self_list) & set(other_list)
        if common_sheet_names == {""}:
            return False

        return True if common_sheet_names else False
