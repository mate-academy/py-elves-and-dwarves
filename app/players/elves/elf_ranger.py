from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        self._nickname = nickname
        self._musical_instrument = musical_instrument
        self._bow_level = bow_level

    def play_elf_song(self) -> None:
        print(f"{self._nickname} is playing a song on the "
              f"{self._musical_instrument}")

    def player_info(self) -> str:
        return (f"Elf ranger {self._nickname}. {self._nickname} "
                f"has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
