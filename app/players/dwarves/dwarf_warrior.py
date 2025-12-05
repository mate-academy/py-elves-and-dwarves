from __future__ import annotations

from players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """Dwarf Warrior class."""

    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._hummer_level: int = int(hummer_level)

    def get_rating(self) -> int:
        """Rating is hummer_level + 4."""
        return self._hummer_level + 4

    def player_info(self) -> str:
        """Return info string for Dwarf Warrior."""
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )
