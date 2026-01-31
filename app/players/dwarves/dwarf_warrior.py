from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """
    Represents the class of dwarf that uses weapons.
    """

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        """
        Initializes a Dwarf character.

        Args:
            nickname (str): Alias for the player (inherited).
            favorite_dish (str): The preferred food of this dwarf (inherited).
            hummer_level (str): Level of the hummer.
        """
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

        def get_rating(
            self
        ) -> int:
            """
            Calculates and returns the character's power rating.
            Returns:
                int: The calculated rating value.
            """
            return self._hummer_level + 4

        def player_info(
            self
        ) -> str:
            """
            Returns a formatted string with the character's full information.

            Returns:
                str: Brief description and stats of the player.
            """
            print(
                f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self._hummer_level} level"
            )
