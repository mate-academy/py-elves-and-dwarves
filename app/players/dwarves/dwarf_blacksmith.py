from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish, skill_level: int):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level