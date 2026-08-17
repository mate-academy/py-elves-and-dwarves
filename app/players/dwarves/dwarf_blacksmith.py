from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """Class representing a Dwarf Blacksmith character."""
    def __init__(self, skill_level: int, nickname: str,
                 favourite_dish: str) -> None:
        """Initialize a DwarfBlacksmith instance.

            :param skill_level: The blacksmithing skill level.
            :type skill_level: int
            :param nickname: The unique nickname of the player.
            :type nickname: str
            :param favourite_dish: The dwarf's favourite dish.
            :type favourite_dish: str
        """
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        """Get the blacksmith's rating based on skill level.

            :return: The skill level of the blacksmith.
            :rtype: int
        """
        return self._skill_level

    def player_info(self) -> str:
        """Return formatted information about the dwarf blacksmith.

            :return: Description of the blacksmith's nickname and skill level.
            :rtype: str
        """
        return (f"Dwarf blacksmith {self.nickname} with "
                f"skill of the {self._skill_level} level")
