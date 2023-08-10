from abc import ABC

from app.players.elves.elf import Elf


class ElfRanger(Elf, ABC):
    def __init__(self, _bow_level, _musical_instrument, nickname):
        super().__init__(_musical_instrument, nickname)
        self.bow_level = _bow_level

    def get_rating(self):
        return self.bow_level * 3

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level")
