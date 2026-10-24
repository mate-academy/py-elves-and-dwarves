from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> str:
        print(
            f"{self._nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )
