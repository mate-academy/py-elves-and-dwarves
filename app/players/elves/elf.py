from app.players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
