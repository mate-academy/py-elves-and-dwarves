from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
    ) -> None:
        self._favourite_dish = favourite_dish
        Dwarf.nickname = nickname

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} "
              f"is eating {self._favourite_dish}")
