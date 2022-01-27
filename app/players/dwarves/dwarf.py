from abc import abstractmethod

from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
