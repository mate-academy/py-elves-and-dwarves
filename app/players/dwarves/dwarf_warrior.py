from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self, nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        name = f"Dwarf warrior {self.nickname}. "
        hummer = f"{self.nickname} has a hummer "
        level = f"of the {self._hummer_level} level"
        return name + hummer + level

    def get_rating(self) -> int:
        return self._hummer_level + 4
