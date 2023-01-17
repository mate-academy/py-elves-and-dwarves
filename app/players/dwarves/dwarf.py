from app.players.player import Player
from abc import ABC


class Dwarf(Player, ABC):
    def __init__(
            self,
            nickname: str = None,
            favourite_dish: str = None
    ) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
