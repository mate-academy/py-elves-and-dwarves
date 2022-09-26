from ..elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level
