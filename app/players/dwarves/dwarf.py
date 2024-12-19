from abc import ABC, abstractmethod

from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str) -> None:
        self.nickname = None
        self._favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")