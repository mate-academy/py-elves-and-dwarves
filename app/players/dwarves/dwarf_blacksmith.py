from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """A class to represent a dwarf blacksmith."""

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        """Initialize the dwarf blacksmith.

        :param nickname: The dwarf blacksmith's nickname.
        :type nickname: str
        :param favourite_dish: The dwarf blacksmith's favourite dish.
        :type favourite_dish: str
        :param skill_level: The dwarf blacksmith's skill level.
        :type skill_level: int
        """
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        """Get the dwarf blacksmith's info.

        :return: The dwarf blacksmith's info.
        :rtype: str
        """
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )

    def get_rating(self) -> int:
        """Get the dwarf blacksmith's rating.

        :return: The dwarf blacksmith's rating.
        :rtype: int
        """
        return self._skill_level
