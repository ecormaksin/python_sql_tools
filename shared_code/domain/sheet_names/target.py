from shared_code.domain.sheet_names._abstract import SheetNames


class TargetSheetNames(SheetNames):
    def contains(self, sheet_name: str) -> bool:
        # 未定義の場合はすべて対象とみなす。
        if not self.value:
            return True

        return super().contains(sheet_name=sheet_name)

    def not_contains(self, sheet_name: str) -> bool:
        return not self.contains(sheet_name=sheet_name)

    def __repr__(self):
        return f"TargetSheetNames('{self.value}')"
