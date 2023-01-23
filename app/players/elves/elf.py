from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str) -> None:
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a "
            f"song on the {self.musical_instrument}"
        )
