from shared_code.domain.sheet_names._abstract import SheetNames


class ExcludeSheetNames(SheetNames):
    def contains(self, sheet_name: str) -> bool:
        # 未定義の場合は除外しない
        if not self.value:
            return False

        return super().contains(sheet_name=sheet_name)
