from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, _favourite_dish: str, nickname: str) -> None:
        super().__init__(nickname)
        self.favourite_dish = _favourite_dish

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.favourite_dish}")
