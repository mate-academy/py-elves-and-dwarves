from __future__ import annotations
from app.players.player import Player


class Elf(Player):
    """Abstract Elf class inherited from Player."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument: str = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
