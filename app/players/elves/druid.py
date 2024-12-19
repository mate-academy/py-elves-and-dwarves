from app.players.elves.elf import Elf
from app.players.player import Player


class Druid(Elf):
    def __init__(self, nickname: str, favourite_spell: str, musical_instrument: str) -> None:
        super().__init__(musical_instrument)
        self._favourite_spell = favourite_spell
        self._nickname = nickname

    def player_info(self) -> str:
        return (f"Druid {self._nickname}. {self._nickname} has a"
                f" favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def play_elf_song(self) -> None:
        print(f"{self._nickname} is playing a song on the {self._musical_instrument}")
