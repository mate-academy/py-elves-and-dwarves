from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):

    def __init__(self, nickname: str, musial_instrument: str) -> None:
        self._musial_instrument = musial_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musial_instrument}")
