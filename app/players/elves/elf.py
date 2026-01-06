from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, _musical_instrument: str) -> None:
        super().__init__(nickname)
        self.musical_instrument = _musical_instrument

    def play_elf_song(self) -> None:
        print(f""
              f"{self.nickname} is playing a song "
              f"on the {self.musical_instrument}")
