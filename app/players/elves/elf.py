from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):
    """Abstract base class for all elf players."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        """Print the elf playing a song on their instrument."""
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )
