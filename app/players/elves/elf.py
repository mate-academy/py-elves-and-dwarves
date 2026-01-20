from app.players.player import Player


class Elf(Player):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str
    ) -> None:
        super().__init__(nickname)
        self.nickname = nickname
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        name = self.nickname
        print(f"{name} is playing a song on the {self._musical_instrument}")
