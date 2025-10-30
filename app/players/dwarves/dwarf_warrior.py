from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """A class to represent a dwarf warrior."""

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        """Initialize the dwarf warrior.

        :param nickname: The dwarf warrior's nickname.
        :type nickname: str
        :param favourite_dish: The dwarf warrior's favourite dish.
        :type favourite_dish: str
        :param hummer_level: The dwarf warrior's hummer level.
        :type hummer_level: int
        """
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        """Get the dwarf warrior's info.

        :return: The dwarf warrior's info.
        :rtype: str
        """
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the "
            f"{self._hummer_level} level"
        )

    def get_rating(self) -> int:
        """Get the dwarf warrior's rating.

        :return: The dwarf warrior's rating.
        :rtype: int
        """
        return self._hummer_level + 4
