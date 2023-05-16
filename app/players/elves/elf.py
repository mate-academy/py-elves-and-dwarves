from app.players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):
    def __init__(self, musical_instrument: int) -> str:
        self._musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a "
            f"song on the {self.musical_instrument}"
        )
