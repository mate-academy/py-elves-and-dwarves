from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(
            self,
            bow_level: int,
            nickname: str,
            musical_instrument: str
    ) -> None:
        self._bow_level = bow_level
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the "
                f"{self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
