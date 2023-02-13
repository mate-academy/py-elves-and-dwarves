from .elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def __str__(self) -> str:
        return f"Elf ranger {self.nickname}."

    def player_info(self) -> str:
        nick = self.nickname
        level = self._bow_level
        return f"{self} {nick} has bow of the {level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
