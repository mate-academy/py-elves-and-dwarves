from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self.musical_instrument = musical_instrument
        super().__init__(nickname=nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song "
              f"on the {self.musical_instrument}")
