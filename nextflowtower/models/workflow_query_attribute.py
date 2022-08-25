from enum import Enum


class WorkflowQueryAttribute(str, Enum):
    OPTIMIZED = "optimized"
    LABELS = "labels"

    def __str__(self) -> str:
        return str(self.value)
