from enum import Enum


class ParticipantType(str, Enum):
    MEMBER = "MEMBER"
    TEAM = "TEAM"
    COLLABORATOR = "COLLABORATOR"

    def __str__(self) -> str:
        return str(self.value)
