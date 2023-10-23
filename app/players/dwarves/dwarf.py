from app.players.player import Player
from abc import abstractmethod


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    @abstractmethod
    def player_info(self) -> str:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
