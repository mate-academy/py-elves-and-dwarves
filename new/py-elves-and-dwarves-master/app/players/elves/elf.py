from app.players.player import Player


class Elf(Player):
    def __init__(self, musical_instrument, nickname):
        super().__init__(nickname)
        self.musical_instrument = musical_instrument


    def play_elf_song(self):
        return f""""{self.nickname} is playing a song on the {self.musical_instrument} """
