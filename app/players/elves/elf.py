from abc import ABC, abstractmethod
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname, musical_instrument):
        super(Elf, self).__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song "
              f"on the {self._musical_instrument}")

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
