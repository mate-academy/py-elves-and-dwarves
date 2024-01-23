from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print("{} is playing a song on the {}"
              .format(self.nickname, self._musical_instrument))
