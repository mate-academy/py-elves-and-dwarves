from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):

    def __init__(self, name, favourite_dish):
        super().__init__(name)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.name} is eating {self._favourite_dish}")
