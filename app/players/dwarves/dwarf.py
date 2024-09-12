from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish, nickname):
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.favourite_dish}")
