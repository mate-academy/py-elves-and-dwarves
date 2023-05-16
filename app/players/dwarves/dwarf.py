from app.players.player import Player
from abc import ABC, abstractmethod


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: int) -> str:
        self._favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
