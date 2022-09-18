from app.players import player


class Elf(player.Player):
    def __init__(self, musical_instrument: str, nickname: str):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        playing_song = " is playing a song on the "
        print(self.nickname + playing_song + self._musical_instrument)
