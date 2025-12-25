from app.players.player import ABC, Player


class Elf(Player, ABC):
    """A base class for all elves."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        """Initialize the elf.

        :param nickname: The elf's nickname.
        :type nickname: str
        :param musical_instrument: The elf's musical instrument.
        :type musical_instrument: str
        """
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        """Play a song on the elf's musical instrument."""
        print(
            f"{self.nickname} is playing a song "
            f"on the {self._musical_instrument}"
        )
