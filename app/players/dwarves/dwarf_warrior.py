from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self, nickname: str, _favourite_dish: str, _hummer_level: str
    ) -> None:
        super().__init__(nickname, _hummer_level)
        self._hummer_level = _hummer_level

    def get_rating(self) -> int:
        return (self._hummer_level + 4)

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}."
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )
