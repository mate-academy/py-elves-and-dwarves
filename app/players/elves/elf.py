from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self.nickname = nickname
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print("{} is playing a song on the {}".format(
            self.nickname,
            self._musical_instrument
        ))
