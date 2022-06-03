from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf, ABC):

    def __init__(self, hummer_level, nickname, favourite_dish):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hummer_level} level"

    def get_rating(self):
        return self._hummer_level + 4
