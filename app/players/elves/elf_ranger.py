from .elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        info = "Elf ranger {0}. {1} has bow of the {2} level"
        return info.format(self.nickname, self.nickname, self._bow_level)

    def get_rating(self) -> int:
        return self._bow_level * 3
