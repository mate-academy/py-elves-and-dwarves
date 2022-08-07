from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):

    def __init__(self, name, music_instrument):
        super().__init__(name)
        self._music_instrument = music_instrument

    def play_elf_song(self):
        print(f"{self.name} is paying a song on the {self._music_instrument}")
