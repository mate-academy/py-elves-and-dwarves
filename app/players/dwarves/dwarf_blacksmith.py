from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def get_rating(self) -> int | None:
        return self.skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level")
