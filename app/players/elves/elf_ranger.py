from .elf import Elf


class ElfRanger(Elf):

    def __init__(
            self,
            bow_level: int,
            nickname: str,
            musical_instrument: str
    ) -> None:
        super().__init__(bow_level)
        self._bow_level = bow_level
        self.nickname += nickname
        self._musical_instrument = musical_instrument

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}." \
               f" {self.nickname} has bow of" \
               f" the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
