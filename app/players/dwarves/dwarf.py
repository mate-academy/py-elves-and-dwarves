from app.players.player import Player
from abc import abstractmethod


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")

        @abstractmethod
        def get_rating(self) -> None:
            pass

        @abstractmethod
        def player_info(self) -> None:
            pass
