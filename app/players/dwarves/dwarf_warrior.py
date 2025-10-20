from __future__ import annotations
from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """Dwarf warrior with a hummer."""

    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level: int = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of "
                f"the {self._hummer_level} level")
