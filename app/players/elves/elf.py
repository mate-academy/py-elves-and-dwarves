from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self._nickname = nickname
        self._musical_instrument = musical_instrument

    @property
    def nickname(self) -> None:
        return self._nickname

    def play_elf_song(self) -> None:
        print(f"{self._nickname} is playing a song "
              f"on the {self._musical_instrument}")
