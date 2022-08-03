from app.players import player
from abc import ABC


class Elf(player.Player, ABC):

    def __init__(self, musical_instrument, nickname):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")
