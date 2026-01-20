from app.players.player import Player


class Elf(Player):
    def __init__(self, _musical_instrument: str, nickname: str) -> None:
        self._musical_instrument = _musical_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} "
              f"is playing a song on the {self._musical_instrument}")
