from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    _hummer_level = 0

    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4
