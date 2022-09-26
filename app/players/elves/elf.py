from app.players.player import Player
from abc import ABC


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str, nickname: str) -> None:
        self.musical_instrument = musical_instrument
        self.nickname = nickname

    def play_elf_song(self):
        print(
            f"{self.nickname} is playing a song"
            f" on the {self.musical_instrument}"
        )
