from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """
    DwarfWarrior class.

    Attributes:
    ___________
    nickname
        the name of the Elf
    favourite_dish
        the Dwarf's favorite dish
    hummer_level
        the Dwarf's hummer level

    Methods:
    _______
    get_rating()
        returns the Dwarf Warrior's hummer level rating

    player_info()
        displays info about Dwarf Warrior

    eat_favorite_dish()
        displays a message about eating a favorite dish
    """
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        """
        Returns the hummer level rating.
        :return: int
        """
        return self._hummer_level + 4

    def player_info(self) -> str:
        """
        Displays a message about the Dwarf Warrior.
        :return: None
        """
        return (f"Dwarf warrior {self.nickname}. "
                f"{self.nickname} has a hummer of the "
                f"{self._hummer_level} level")
