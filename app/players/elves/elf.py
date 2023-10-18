from app.players.player import Player


class Elf(Player):
    def __init__(self, _musical_instrument: str) -> None:
        super().__init__()
        self._musical_instrument = _musical_instrument

    def play_elf_song(self) -> None:
        return f"{self.nickname} is playing a \
            song on the {self._musical_instrument}"
