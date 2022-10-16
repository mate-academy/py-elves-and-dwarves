from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish: str, hummer_level: int):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hummer_level} level"

    def get_rating(self):
        return 4 + self._hummer_level
