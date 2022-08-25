from enum import Enum


class OrgRole(str, Enum):
    OWNER = "owner"
    MEMBER = "member"
    COLLABORATOR = "collaborator"

    def __str__(self) -> str:
        return str(self.value)
