from ..player import Player


class Elf(Player):
    def __init__(self, _musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = _musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a "
              f"song on the {self._musical_instrument}")
