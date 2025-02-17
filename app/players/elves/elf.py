from ..player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> str:
        print(f"{self.nickname} is "
              f"playing a song on the {self._musical_instrument}")
