from .elf import Elves


class ElfRanger(Elves):
    def __init__(self, _musical_instrument: str,
                 nickname: str, _bow_level: int) -> None:
        super().__init__(_musical_instrument, nickname)
        self._bow_level = _bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
