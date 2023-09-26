from app.players.elves.elf import Elf
from abc import ABC


class ElfRanger(Elf, ABC):
    def __init__(self, nickname, musical_instrument, bow_level):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the " \
               f"{self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level
