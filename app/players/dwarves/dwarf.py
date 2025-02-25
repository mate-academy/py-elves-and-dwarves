from app.players.player import Player


from abc import ABC, abstractmethod


class Dwarf(Player, ABC):
    @abstractmethod
    def __init__(self, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self) -> None:
        print(f"{self._nickname} is eating {self._favourite_dish}")
