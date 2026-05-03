from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> None:
        name = self.nickname
        music = self._musical_instrument
        print(f"{name} is playing a song on the {music}")
