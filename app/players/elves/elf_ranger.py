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

    def player_info(self) -> str:
        text_1 = f"Elf ranger {self.nickname}. {self.nickname} "
        text_2 = f"has bow of the {self._bow_level} level"

        return text_1 + text_2

    def get_rating(self) -> int:
        return 3 * self._bow_level
