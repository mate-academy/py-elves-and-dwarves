from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
