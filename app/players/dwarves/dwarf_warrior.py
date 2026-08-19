from typing import override

from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level: int = hummer_level

    @override
    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"  # noqa: E501

    @override
    def get_rating(self) -> int:
        return self._hummer_level + 4
