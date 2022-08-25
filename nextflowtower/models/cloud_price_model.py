from enum import Enum


class CloudPriceModel(str, Enum):
    STANDARD = "standard"
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
