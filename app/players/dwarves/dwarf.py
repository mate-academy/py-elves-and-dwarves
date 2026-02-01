from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    """
    Represents the base class for all dwarf character types.
    """

    def __init__(
        self,
        nickname: str,
        favourite_dish: str
    ) -> None:
        """
        Initializes a Dwarf character.

        Args:
            nickname (str): Alias for the player (inherited).
            favorite_dish (str): The preferred food of this dwarf types.
        """
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(
        self
    ) -> None:
        """
        Prints a message indicating the dwarf is eating their favourite dish.
        """
        print(f"{self.nickname} is eating {self._favourite_dish}")
