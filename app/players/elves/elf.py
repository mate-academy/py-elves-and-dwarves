from app.players.player import Player


class Elf(Player):
    elves = []

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument
        Elf.elves.append(self)

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )
