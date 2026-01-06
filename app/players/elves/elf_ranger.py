from app.players.elves import elf


class ElfRanger(elf.Elf):
    def __init__(self, bow_level: int, nickname, musical_instrument):
        self._bow_level = bow_level
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} has " \
               f"bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
