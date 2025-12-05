from __future__ import annotations

from players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """Dwarf Blacksmith class."""

    def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._skill_level: int = int(skill_level)

    def get_rating(self) -> int:
        """Rating is the skill_level."""
        return self._skill_level

    def player_info(self) -> str:
        """Return info string for Dwarf Blacksmith."""
        return (
            f"Dwarf blacksmith {self.nickname} with skill of the "
            f"{self._skill_level} level"
        )
