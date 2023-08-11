from abc import ABC
from app.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf, ABC):
    def __init__(self, _hummer_level: int,
                 _favourite_dish: str, nickname: str) -> None:
        super().__init__(_favourite_dish, nickname)
        self.hummer_level = _hummer_level

    def get_rating(self) -> int:
        return self.hummer_level + 4

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. "
              f"{self.nickname} has a hummer of the {self.hummer_level} level")
