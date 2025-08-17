from dataclasses import dataclass


@dataclass(frozen=True)
class SourceDataXlsxFilePath:
    value: str

    def __post_init__(self):
        if type(self.value) is not str or not self.value:
            raise ValueError("SourceDataXlsxFilePath must be specified.")

    def __eq__(self, other):
        if not isinstance(other, SourceDataXlsxFilePath):
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"SourceDataXlsxFilePath(value={self.value})"
