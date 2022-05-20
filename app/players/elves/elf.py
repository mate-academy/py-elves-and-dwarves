"""
This is specific class for the elf`s race.
It inherits from the Player class, and
provides additional method for every elf
of any type.
"""


from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")
