from app.players.elves.elf import Elf


class Druid(Elf):
    """Concrete class representing a Druid elf."""
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        """
        Initialize a Druid elf object with
        nickname, musical_instrument and favourite_spell.
        """
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        """
        Calculate and return the druid's rating
        based on the length of their favourite spell.
        """
        return len(self._favourite_spell)

    def player_info(self) -> str:
        """
        Return a string with the druid's detailed information.
        """
        return (f"Druid {self.nickname}. {self.nickname}"
                f" has a favourite spell: {self._favourite_spell}")
