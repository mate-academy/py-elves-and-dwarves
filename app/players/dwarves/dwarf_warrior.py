from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """Class representing a Dwarf Warrior character."""
    def __init__(self, hummer_level: int, nickname: str,
                 favourite_dish: str) -> None:
        """Initialize a DwarfWarrior instance.

            :param hummer_level: The level of the warrior's hammer.
            :type hummer_level: int
            :param nickname: The unique nickname of the dwarf.
            :type nickname: str
            :param favourite_dish: The dwarf's favourite dish.
            :type favourite_dish: str
        """
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        """Get the warrior's rating based on hammer level.

            :return: The rating calculated from hammer level plus bonus.
            :rtype: int
        """
        return self._hummer_level + 4

    def player_info(self) -> str:
        """Return formatted information about the dwarf warrior.

            :return: Description of the warrior's nickname and hammer level.
            :rtype: str
        """
        return (f"Dwarf warrior {self.nickname}. {self.nickname} has a "
                f"hummer of the {self._hummer_level} level")
