from .dwarf import Dwarf

class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish, hummer_level):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self):
        return self._hummer_level + 4

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"
