from ..player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        print(nickname)
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing "
              f"a song on the {self._musical_instrument}")
