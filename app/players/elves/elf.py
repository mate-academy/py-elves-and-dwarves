from app.players import player


class Elf(player.Player):
    def __init__(self, nickname, musical_instrument):
        self._musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self):
        print(f"{self.nickname} is playing "
              f"a song on the {self._musical_instrument}")
