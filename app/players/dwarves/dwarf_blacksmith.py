from app.players.dwarves.dwarf import Dwarf
from abc import ABC


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self, nickname, favourite_dish, skill_level):
        self._skill_level = skill_level
        super().__init__(nickname, favourite_dish)

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname}" \
               f" with skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
