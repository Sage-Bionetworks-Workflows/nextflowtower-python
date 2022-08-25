from enum import Enum


class ForgeConfigType(str, Enum):
    SPOT = "SPOT"
    EC2 = "EC2"

    def __str__(self) -> str:
        return str(self.value)
