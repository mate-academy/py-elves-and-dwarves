from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song on the "
            f"{self.musical_instrument}"
        )
