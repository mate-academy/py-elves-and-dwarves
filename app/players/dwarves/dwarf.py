from app.players.player import Player
from abc import abstractclassmethod


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    @abstractclassmethod
    def eat_favourite_dish(self) -> None:
        pass
