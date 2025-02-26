from app.players.player import Player


class Elf(Player):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        long_string = f"{self.nickname} "
        long_string += "is playing a song "
        long_string += f"on the {self._musical_instrument}"
        print(long_string)
