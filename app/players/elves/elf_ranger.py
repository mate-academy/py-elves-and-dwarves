from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self, nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        self._musical_instrument = musical_instrument
        self._bow_level = bow_level
        super().__init__(nickname, musical_instrument)

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
                f"{self._bow_level} level")

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")
