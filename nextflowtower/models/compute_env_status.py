from enum import Enum


class ComputeEnvStatus(str, Enum):
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    ERRORED = "ERRORED"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
