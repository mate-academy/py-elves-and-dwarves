from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self.nickname = nickname
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")
