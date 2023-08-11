from abc import ABC
from app.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self, _skill_level: str, _favourite_dish: str,
                 nickname: str) -> None:
        super().__init__(_favourite_dish, nickname)
        self.skill_level = _skill_level

    def get_rating(self) -> str:
        return self.skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the "
              f"{self.skill_level} level")
