from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """
    Represents the class of dwarf who is master of blacksmithing
    """

    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        skill_level: int
    ) -> None:
        """
        Initializes a Dwarf character.

        Args:
            nickname (str): Alias for the player (inherited).
            favorite_dish (str): The preferred food of this dwarf (inherited).
            skill_level (int): Level of the blacksmith skill.
        """
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(
        self
    ) -> int:
        """
        Calculates and returns the character's power rating.

        Returns:
            int: The calculated rating value.
        """
        return self._skill_level

    def player_info(
        self
    ) -> str:
        """
        Returns a formatted string with the character's full information.

        Returns:
            str: Brief description and stats of the player.
        """
        print(
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )
