from app.players.player import Player


class Elf(Player):
    def __init__(self, musical_instrument: str, nickname: str) -> None:
        self.__musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.__musical_instrument}")
