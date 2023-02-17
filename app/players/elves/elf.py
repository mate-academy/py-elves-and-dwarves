from abc import ABC

from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> str:
        print(f"{self.nickname} is "
              f"playing a song on "
              f"the {self.musical_instrument}")
