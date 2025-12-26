from app.players.player import Player


class Elf(Player):
    def __init__(self,
                 musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
