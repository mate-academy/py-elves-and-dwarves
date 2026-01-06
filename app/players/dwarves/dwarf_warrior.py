from app.players.dwarves import dwarf


class DwarfWarrior(dwarf.Dwarf):
    def __init__(self, hummer_level: int, nickname, favourite_dish):
        self._hummer_level = hummer_level
        super().__init__(nickname, favourite_dish)

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has " \
               f"a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4
