from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):

    def __init__(self, skill_level, nickname, favourite_dish):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with " \
               f"skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
