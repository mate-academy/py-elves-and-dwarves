"""
This is specific class for the dwarf`s race.
It inherits from the Player class, and
provides additional method for every dwarf
of any type.
"""


from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
