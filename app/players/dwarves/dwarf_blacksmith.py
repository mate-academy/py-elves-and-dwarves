# flake8: noqa: E501, W293
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> None:
        return self._skill_level
