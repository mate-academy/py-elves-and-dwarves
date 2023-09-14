from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self.musical_instrument = musical_instrument

    @property
    def musical_instrument(self) -> str:
        return self._musical_instrument

    @musical_instrument.setter
    def musical_instrument(self, value: str) -> None:
        self._musical_instrument = value

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song "
              f"on the {self.musical_instrument}")
