from app.players.elves.elf import Elf
from abc import ABC


class ElfRanger(Elf, ABC):
    def __init__(self, nickname, musical_instrument, bow_level):
        self._bow_level = bow_level
        super().__init__(nickname, musical_instrument)

    def player_info(self):
        return f"Elf ranger {self.nickname}." \
               f" {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level
