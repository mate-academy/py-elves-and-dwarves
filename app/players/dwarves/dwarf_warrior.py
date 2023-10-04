from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self, favourite_dish: str, nickname: str, hummer_level: int
    ) -> None:
        self._hummer_level = hummer_level
        super().__init__(favourite_dish, nickname)

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. " \
               f"{self.nickname} has a hummer of the " \
               f"{self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4
