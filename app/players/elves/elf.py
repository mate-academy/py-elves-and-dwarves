from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str):
        self.nickname = nickname
        self.musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on "
              f"the {self.musical_instrument}")
