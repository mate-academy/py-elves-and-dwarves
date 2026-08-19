from typing import override

from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        skill_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level: int = skill_level

    @override
    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"  # noqa: E501

    @override
    def get_rating(self) -> int:
        return self._skill_level
