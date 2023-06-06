from app.players.player import Player


class Elf(Player):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        nickname = self.nickname
        musical_instrument = self._musical_instrument
        print(f"{nickname} is playing a song on the {musical_instrument}")
