from app.players.player import Player


class Elf(Player):

    def __init__(self, nickname: str, musical_instrumente: str) -> None:
        super().__init__(nickname)
        self._musical_instrumente = musical_instrumente

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrumente}")
