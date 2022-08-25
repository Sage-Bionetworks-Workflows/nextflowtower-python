from enum import Enum


class PipelineQueryAttribute(str, Enum):
    OPTIMIZED = "optimized"
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
