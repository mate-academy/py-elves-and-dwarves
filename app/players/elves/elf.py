from app.players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):

    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is"
              f" playing a song on the {self._musical_instrument}")

    @abstractmethod
    def player_info(self):
        pass

    @abstractmethod
    def get_rating(self):
        pass
