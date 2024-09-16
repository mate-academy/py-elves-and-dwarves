from app.players.dwarves.dwarf import Dwarf
from abc import ABC


class DwarfWarrior(Dwarf, ABC):
    def __init__(self, nickname, favourite_dish, hummer_level):
        self._hummer_level = hummer_level
        super().__init__(nickname, favourite_dish)

    def player_info(self):
        return f"Dwarf warrior {self.nickname}." \
               f" {self.nickname}" \
               f" has a hummer of the {self._hummer_level} level"

    def get_rating(self):
        return 4 + self._hummer_level
