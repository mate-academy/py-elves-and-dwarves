from abc import ABCMeta, abstractmethod

from app.players.player import Player


class Elf(Player, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song "
            f"on the {self._musical_instrument}"
        )
