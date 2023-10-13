from ..player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        play_song = "{0} is playing a song on the {1}"
        print(play_song.format(self.nickname, self._musical_instrument))
