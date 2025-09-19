from abc import ABC
from ..player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        # 1 quebra de linha: o print já acrescenta '\n'
        print(f"{self.nickname} is eating {self.favourite_dish}")
