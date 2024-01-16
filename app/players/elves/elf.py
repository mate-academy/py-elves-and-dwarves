from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        elf_nick_str = f"{self.nickname} is playing a song"
        elf_musical_instrument_str = f"on the {self._musical_instrument}"
        print(f"{elf_nick_str} {elf_musical_instrument_str}")
