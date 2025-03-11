from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):

    def __init__(self, nick_name: str, favourite_dish: str) -> None:
        super().__init__(nick_name)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
