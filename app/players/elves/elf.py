from abc import ABC
from app.players.player import Player


class Elf(ABC, Player):
    def __init__(self, musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname=nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")
