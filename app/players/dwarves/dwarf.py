from abc import ABC

from app.players.player import Player


class Dwarf(ABC, Player):
    _favourite_dish: str

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
