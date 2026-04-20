from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):
    """Abstract base class for all dwarf players."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Print the dwarf eating their favourite dish."""
        print(f"{self.nickname} is eating {self._favourite_dish}")
