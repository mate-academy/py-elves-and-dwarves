from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(self, favourite_dish, nickname, hummer_level: int):
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def get_rating(self):
        return self._hummer_level + 4

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. " \
               f"{self.nickname} has a hummer " \
               f"of the {self._hummer_level} level"
