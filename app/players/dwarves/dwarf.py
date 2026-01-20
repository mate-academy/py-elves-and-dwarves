from app.players import player
from abc import ABC


class Dwarf(player.Player, ABC):

    def __init__(self, favourite_dish, nickname):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
