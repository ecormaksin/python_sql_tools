from dataclasses import dataclass


@dataclass(frozen=True)
class DMLs:
    value: list[str]

    @property
    def number_of_lines(self) -> int:
        return len(self.value)
