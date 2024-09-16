from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument):
        self._musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self):
        print(f"{self.nickname}"
              f" is playing a song on the {self._musical_instrument}")
