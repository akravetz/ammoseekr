from dataclasses import dataclass
from enum import StrEnum


@dataclass
class Caliber:
    readable_name: str
    id: int
    gun_type: str


PISTOL_9MM = Caliber("9mm-luger", "82", "handgun")
RIFLE_556 = Caliber("5.56x45mm-nato", "352", "rifle")
RIFLE_300_BO = Caliber("300aac-blackout", "332", "rifle")


class Casing(StrEnum):
    BRASS = "brass"
    STEEL = "steel"


class Condition(StrEnum):
    NEW = "new"
    USED = "user"
