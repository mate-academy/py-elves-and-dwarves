from abc import ABC, abstractmethod
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self):
        pass
