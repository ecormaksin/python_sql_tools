from dataclasses import dataclass

from shared_code.domain.dmls.entity import OneTableDmls


@dataclass(frozen=True)
class AllTableDMLs:
    elements: list[OneTableDmls]

    @classmethod
    def empty(cls) -> "AllTableDMLs":
        return cls(elements=[])

    def append(self, element: OneTableDmls) -> "AllTableDMLs":
        copied = list(self.elements)
        copied.append(element)
        return self.__class__(elements=copied)

    @property
    def unmodifiable_elements(self) -> list[OneTableDmls]:
        return list(self.elements)
