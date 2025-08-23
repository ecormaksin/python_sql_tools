from typing import Optional
from dataclasses import dataclass

from shared_code.application.app_config.builder.base.builder import AbstractBuilder
from shared_code.application.app_config.builder.base.result import (
    AbstractBuildResult,
)
from shared_code.domain.table_name_definition_type import TableNameDefinitionType
from shared_code.application.app_config.validation.result_flag import (
    AppConfigValidationResultFlag as ValidationResultFlag,
)


@dataclass(frozen=True)
class TableNameDefinitionTypeBuildResult(AbstractBuildResult):
    table_name_definition_type: Optional[TableNameDefinitionType]


BuildResult = TableNameDefinitionTypeBuildResult


class TableNameDefinitionTypeBuilder(AbstractBuilder):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, a_traceback):
        """
        do nothing
        """

    def execute(self) -> BuildResult:
        table_name_definition_type = self.__get_table_name_definition_type()

        return BuildResult(
            table_name_definition_type=table_name_definition_type,
            error_messages=super().error_messages,
        )

    def __get_table_name_definition_type(self) -> Optional[TableNameDefinitionType]:
        config_data = super().config_data
        property_name = "table_name"

        result_flag = super().validate_required_property(property_name=property_name)
        if result_flag == ValidationResultFlag.NG:
            return None

        try:
            table_name_definition_type = TableNameDefinitionType.of(
                config_data[property_name]
            )
            return table_name_definition_type
        except KeyError:
            error_messages = super().error_messages
            error_messages.append(
                f"The property '{property_name}' must be specified with one of the following values: sheet, cell."
            )
            super().replace_error_messages(error_messages=error_messages)
            return None
