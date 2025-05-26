from .elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def get_rating(self) -> float:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self._bow_level} level")
