from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int | float) -> None:
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. {self.nickname}"
                f" has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> float:
        return self._hummer_level + 4
