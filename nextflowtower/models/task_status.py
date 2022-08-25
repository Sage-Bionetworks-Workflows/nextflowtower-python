from enum import Enum


class TaskStatus(str, Enum):
    NEW = "NEW"
    SUBMITTED = "SUBMITTED"
    RUNNING = "RUNNING"
    CACHED = "CACHED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"

    def __str__(self) -> str:
        return str(self.value)
