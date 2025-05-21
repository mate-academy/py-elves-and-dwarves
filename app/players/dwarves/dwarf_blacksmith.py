from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level