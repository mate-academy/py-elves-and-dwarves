from abc import ABC

from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf, ABC):
    def __init__(self, _hummer_level, _favourite_dish, nickname):
        super().__init__(_favourite_dish, nickname)
        self.hummer_level = _hummer_level

    def get_rating(self):
        return self.hummer_level + 4

    def player_info(self):
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level")
