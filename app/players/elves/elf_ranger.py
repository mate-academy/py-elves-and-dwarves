from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """Concrete class representing an Elf ranger."""
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        """
        Initialize an ElfRanger object with
        nickname, musical instrument and bow level.
        """
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        """
        Calculate and return the elf ranger's rating based on bow level.
        """
        return 3 * self._bow_level

    def player_info(self) -> str:
        """
        Return a string with the elf ranger's detailed information.
        """
        return (f"Elf ranger {self.nickname}. {self.nickname}"
                f" has bow of the {self._bow_level} level")
