from app.players.player import Player
from abc import ABC


class Dwarf(Player, ABC):
    def __init__(self, nickname, favourite_dish):
        self.favourite_dish = favourite_dish
        super().__init__(nickname)

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.favourite_dish}")
