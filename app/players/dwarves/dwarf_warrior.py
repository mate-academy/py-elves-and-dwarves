from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, _hummer_level: str) -> None:
        self._hummer_level = _hummer_level

    def get_rating(self) -> int:
        return (self._hummer_level + 4)

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}."
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )
