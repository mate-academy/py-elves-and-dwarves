from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, favourite_dish, hummer_level, nickname):
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}." \
               f" {self.nickname} has a hummer of the" \
               f" {self._hummer_level} level"

    def get_rating(self):
        return self._hummer_level + 4
