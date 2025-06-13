from app.players.player import Player


class Elf(Player):
    def __init__(self, musical_instrument: str, nickname: str):
        super().__init__(nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a "
              f"song on the {self.musical_instrument}")
