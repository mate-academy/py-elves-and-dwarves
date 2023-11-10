from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.__favourite_dish__ = favourite_dish

    def eat_favourite_dish(self) -> None:
        return print(
            f"{self.nickname} is eating "
            f"{self.__favourite_dish__}"
        )
