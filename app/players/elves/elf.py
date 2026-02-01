from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    """
    Represents the base class for all elves character types.
    """

    def __init__(
        self,
        nickname: str,
        musical_instrument: str
    ) -> None:
        """
        Initializes a Elf character.

        Args:
            nickname (str): Alias for the player (inherited).
            musical_instrument (str): The preferred instrument of this elf.
        """
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(
        self
    ) -> None:
        """
        Prints a message indicating the elf is playing with the instrument.
        """
        print(f"{self.nickname} is playing a song on the {
              self._musical_instrument}")
