from enum import Enum


class PipelineSchemaAttributes(str, Enum):
    SCHEMA = "schema"
    PARAMS = "params"

    def __str__(self) -> str:
        return str(self.value)
