from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):

    def __init__(self, nickname, favourite_dish, skill_level):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"" \
               f"Dwarf blacksmith {self.nickname} with skill of the " \
               f"{self._skill_level} level"

    def get_rating(self):
        return self._skill_level
