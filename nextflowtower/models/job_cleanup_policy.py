from enum import Enum


class JobCleanupPolicy(str, Enum):
    ON_SUCCESS = "on_success"
    ALWAYS = "always"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
