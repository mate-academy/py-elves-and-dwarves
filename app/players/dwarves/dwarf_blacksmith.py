from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """
    DwarfBlacksmith class.

    Attributes:
    ___________
    nickname
        the name of the Elf
    favourite_dish
        the Dwarf's favorite dish
    skill_level
        the level of Dwarf Blacksmith's skill_level

    Methods:
    _______
    get_rating()
        returns the Dwarf Blacksmith's level rating

    player_info()
        displays info about Dwarf Blacksmith

    eat_favorite_dish()
        displays a message about eating a favorite dish
    """
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self._skill_level = skill_level

    def get_rating(self) -> int:
        """
        Returns the Dwarf Blacksmith's skill level.
        :return: int
        """
        return self._skill_level

    def player_info(self) -> str:
        """
        Displays a message about the Dwarf Blacksmith.
        :return: None
        """
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self._skill_level} level")
