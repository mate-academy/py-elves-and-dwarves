from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument: str = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a "
              f"song on the {self.musical_instrument}")

    @property
    def musical_instrument(self) -> str:
        return self._musical_instrument
