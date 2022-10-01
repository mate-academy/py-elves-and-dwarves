from app.players.player import Player


class Elf(Player):

    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        mus_instrument = self._musical_instrument
        print(f"{self.nickname} is playing a song on the {mus_instrument}")
