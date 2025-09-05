from abc import ABC

from app.players.player import Player


class Elf(ABC, Player):
    _musical_instrument: str

    def play_elf_song(self) -> None:
        print(f"{self.nickname} "
              f"is playing a song on the {self._musical_instrument}")
