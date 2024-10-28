from abc import abstractmethod
from app.players.player import Player


class Elf(Player):
    @abstractmethod
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> None:
        print(f"{self.nickname} is "
              f"playing a song on the {self._musical_instrument}")
