from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):

    def __init__(
            self,
            musical_instrument: str,
            nickname: str
    ) -> None:
        self._musical_instrument = musical_instrument
        super().__init__(nickname=nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")
