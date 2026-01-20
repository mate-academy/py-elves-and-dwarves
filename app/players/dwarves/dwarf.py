from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str, nickname: str) -> None:
        super().__init__(nickname)
        self.fav_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.fav_dish}")
