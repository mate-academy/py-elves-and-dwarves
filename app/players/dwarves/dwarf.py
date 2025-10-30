from app.players.player import ABC, Player


class Dwarf(Player, ABC):
    """A base class for all dwarves."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        """Initialize the dwarf.

        :param nickname: The dwarf's nickname.
        :type nickname: str
        :param favourite_dish: The dwarf's favourite dish.
        :type favourite_dish: str
        """
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Eat the dwarf's favourite dish."""
        print(
            f"{self.nickname} is eating"
            f" {self._favourite_dish}"
        )
