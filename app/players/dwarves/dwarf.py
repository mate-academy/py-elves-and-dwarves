from abc import ABC, abstractmethod
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname, favourite_dish: str):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        return f"{self.nickname} is eating {self._favourite_dish}\n"

