from ..player import Player

class Elf(Player):
    def __init__(self, nickname:str, musical_instrument: str ) -> None:
        super().__init(nickname)
        self.musical_instrument = musical_instrument
    
    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")