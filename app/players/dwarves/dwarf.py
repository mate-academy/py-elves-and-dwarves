from app.players.player import Player
from abc import abstractmethod


@abstractmethod
class Dwarf(Player):
    def __init__(self, nickname: str, favorite_dish: str) -> None:
        super().__init__(nickname)
        self._favorite_dish = favorite_dish


    def eat_favorite_dish(self) -> str:
        print(f"{self.nicckname} is eating {self._favorite_dish}")