from abc import ABC, abstractmethod
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self):
        pass
