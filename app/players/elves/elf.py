from app.players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):
    @abstractmethod
    def __init__(self, _musical_instrument, nickname):
        super().__init__(nickname)
        self.musical_instrument = _musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

