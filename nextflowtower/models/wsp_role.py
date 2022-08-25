from enum import Enum


class WspRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MAINTAIN = "maintain"
    LAUNCH = "launch"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
