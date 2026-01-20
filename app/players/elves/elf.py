from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument : str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        nnam = self.nickname
        mus = self._musical_instrument
        print(f"{nnam} is playing a song on the {mus}")
