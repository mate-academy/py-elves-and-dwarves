from __future__ import annotations

from typing import Any

from players.player import Player


class Elf(Player):
    """Abstract Elf base class."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        # atributo protegido conforme solicitado
        self._musical_instrument: str = musical_instrument

    def play_elf_song(self) -> None:
        """Prints the elf song action."""
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
