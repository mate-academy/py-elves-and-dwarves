from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):

    _musical_instrument: str

    def __init__(self,
                 name: str,
                 musical_instrument: str) -> None:
        self.nickname = name
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")
