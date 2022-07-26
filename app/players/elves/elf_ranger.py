from abc import ABC
from app.players.elves.elf import Elf


class ElfRanger(Elf, ABC):
    def __init__(self, nickname, musical_instrument, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return self._bow_level * 3

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} has "
              f"bow of the {self._bow_level} level")
