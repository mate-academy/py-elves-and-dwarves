from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):
    def __init__(self, _musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname)
        self.musical_instrument = _musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")
