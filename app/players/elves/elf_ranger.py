from abc import ABC
from app.players.elves.elf import Elf


class ElfRanger(Elf, ABC):

    def __init__(self, name, bow_level: int):
        super().__init__(name)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.name}. {self.name} has bow of the {self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level
