from abc import ABC
from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf, ABC):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level