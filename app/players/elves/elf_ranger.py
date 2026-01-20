from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:

        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (f"Elf ranger "
                f"{self.nickname}. "
                f"{self.nickname} "
                f"has bow of the "
                f"{self._bow_level}"
                f" level")
