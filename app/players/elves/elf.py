from app.main import Player, ABC


class Elf(ABC, Player):
    def __init__(self, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a"
              f" song on the {self._musical_instrument}")
