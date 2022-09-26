from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    def play_elf_song(self) -> None:
        print(f"{self.nickname}"
              f" is playing a song on the {self.musical_instrument}")
