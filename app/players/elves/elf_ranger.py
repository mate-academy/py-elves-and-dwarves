from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """
    Represents the class of elf that uses a bow.
    """

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        bow_level: int
    ) -> None:
        """
        Initializes an Elf Ranger character.

        Args:
            nickname (str): Alias for the player (inherited).
            musical_instrument (str): Instrument that the player chosen.
            bow_level (int): Level of the weapon.
        """
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(
        self
    ) -> int:
        """
        Calculates and returns the character's power rating.

        Returns:
            int: The calculated rating value.
        """
        return self._bow_level * 3

    def player_info(
        self
    ) -> str:
        """
        Returns a formatted string with the character's full information.

        Returns:
            str: Brief description and stats of the player.
        """
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )
