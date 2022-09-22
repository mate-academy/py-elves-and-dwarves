from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level, favourite_dish, nickname):
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self):
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level")

    def get_rating(self):
        return self._hummer_level + 4
