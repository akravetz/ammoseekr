from enum import StrEnum


class Caliber(StrEnum):
    PISTOL_9MM = "9mm-luger"
    RIFLE_556_NATO = "5.56x45mm-nato"
    RIFLE_300_BO = "300aac-blackout"


class Casing(StrEnum):
    BRASS = "brass"
    STEEL = "steel"


class Condition(StrEnum):
    NEW = "new"
    USED = "user"
