from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):

    def __init__(self, name, skill_level: int):
        super().__init__(name)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.name} with skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
