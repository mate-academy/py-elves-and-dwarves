from abc import ABC, abstractmethod

from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str) -> None:
        self.nickname = None
        self._musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song "
              f"on the {self._musical_instrument}")
