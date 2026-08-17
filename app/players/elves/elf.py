from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):
    """Abstract base class for all Elf characters."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        """Initialize an Elf instance.

            :param nickname: The unique nickname of the elf.
            :type nickname: str
            :param musical_instrument: The instrument the elf plays.
            :type musical_instrument: str
        """
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        """Play a song on the elf's musical instrument."""
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}")
