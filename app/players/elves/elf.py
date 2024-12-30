from ..player import Player

class Elf(Player):
    def __init__(self, _musical_instrument, nickname):
        super().__init__(nickname)
        self._musical_instrument = _musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


