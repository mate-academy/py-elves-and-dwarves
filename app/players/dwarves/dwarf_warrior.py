from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self, nickname: str,
        favourite_dish: str,
        hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level: int = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self.hummer_level} level")

    def get_rating(self) -> int:
        return self.hummer_level + 4

    @property
    def hummer_level(self) -> int:
        return self._hummer_level
