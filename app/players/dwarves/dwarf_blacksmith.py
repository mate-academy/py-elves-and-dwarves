from __future__ import annotations

from app.players import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int):
        super().__init__(nickname, favourite_dish)
        self._skill_level = int(skill_level)

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} with skill of the "
            f"{self._skill_level} level"
        )
