from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    """Abstrakcyjna klasa krasnoluda, dziedzicząca po Player i ABC."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Krasnolud je swoje ulubione danie."""
        print(f"{self.nickname} is eating {self._favourite_dish}")
