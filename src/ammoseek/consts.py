from enum import Enum


class Caliber(str, Enum):
    PISTOL_9MM = "9mm-luger"
    RIFLE_556_NATO = "5.56x45mm-nato"
    RIFLE_300_BO = "300aac-blackout"

    def __str__(self):
        return self.value


class Casing(str, Enum):
    BRASS = "brass"
    STEEL = "steel"

    def __str__(self):
        return self.value


class Condition(str, Enum):
    NEW = "new"
    USED = "user"

    def __str__(self):
        return self.value
