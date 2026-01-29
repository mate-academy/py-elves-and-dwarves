from app.players.elves.elf import Elf


class Druid(Elf):
    """
    Represents the class of elf that can cast magic.
    """

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        """
        Initializes Druid elf character.

        Args:
            nickname (str): Alias for the player (inherited).
            musical_instrument (str): Instrument that the player chosen.
            favourite_spell (str): favourite magic.
        """
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(
        self
    ) -> int:
        """
        Calculates and returns the character's power rating.

        Returns:
            int: Count how many characters the spell has.
        """
        return len(self._favourite_spell)

    def player_info(
        self
    ) -> str:
        """
        Returns a formatted string with the character's full information.

        Returns:
            str: Brief description and stats of the player.
        """
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
        )
