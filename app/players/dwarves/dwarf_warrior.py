from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 favourite_dish: str,
                 hummer_level: int,
                 nickname: str) -> None:
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}." \
               f" {self.nickname}" \
               f" has a hummer of the {self._hummer_level} level"
