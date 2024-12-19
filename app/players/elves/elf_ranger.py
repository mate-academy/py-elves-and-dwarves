from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str, bow_level: int, musical_instrument: str):
        super().__init__(musical_instrument)
        self._bow_level = bow_level
        self._nickname = nickname

    def player_info(self) -> str:
        return f"Elf ranger {self._nickname}. {self._nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def play_elf_song(self) -> None:
        print(f"{self._nickname} is playing a song on the {self._musical_instrument}")
