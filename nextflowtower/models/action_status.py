from enum import Enum


class ActionStatus(str, Enum):
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
