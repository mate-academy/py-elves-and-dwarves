from abc import ABC

from app.players.elves.elf import Elf


class Druid(Elf, ABC):
    def __init__(self, _favourite_spell, _musical_instrument, nickname):
        super().__init__(_musical_instrument, nickname)
        self.favourite_spell = _favourite_spell

    def get_rating(self):
        return len(self.favourite_spell)

    def player_info(self):
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}")
