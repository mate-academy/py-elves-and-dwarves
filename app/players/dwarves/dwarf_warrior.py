from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            _favourite_dish: str,
            _hummer_level: int
    ) -> None:
        super().__init__(nickname, _favourite_dish)
        self._hummer_level = _hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. \
            {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> None:
        return self._hummer_level + 4
