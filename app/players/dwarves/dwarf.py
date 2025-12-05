from __future__ import annotations

from players.player import Player


class Dwarf(Player):
    """Abstract Dwarf base class."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish: str = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Prints the dwarf eating action."""
        print(f"{self.nickname} is eating {self._favourite_dish}")
