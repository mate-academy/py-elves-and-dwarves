from abc import ABC, abstractmethod
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument: str):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        return f"{self.nickname} is playing a song on the {self._musical_instrument}"
