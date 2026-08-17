from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):
    """Abstract base class for all Dwarf characters."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        """Initialize a Dwarf instance.

            :param nickname: The unique nickname of the player.
            :type nickname: str
            :param favourite_dish: The dwarf's favourite dish.
            :type favourite_dish: str
        """
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Eat the dwarf's favourite dish."""
        print(f"{self.nickname} is eating {self._favourite_dish}")
