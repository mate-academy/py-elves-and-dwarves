from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):

    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self.__favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.__favourite_dish}")
