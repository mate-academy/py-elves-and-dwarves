from abc import ABC, abstractmethod
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self):
        pass
