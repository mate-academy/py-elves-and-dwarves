from player import Player


class Elf(Player):
    def __init__(self, name: str, musical_instrument: str) -> None:
        super().__init(name)
        self._musical_instrument = musical_instrument
    
    def play_elf_song(self) -> None:
        print(f"{self.name} is playing a song on the {self._musical_instrument}")

