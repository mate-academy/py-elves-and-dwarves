from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, music_instrument: str) -> None:
        super().__init__(nickname)
        self._music_instrument = music_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song"
              f" on the {self._music_instrument}")
