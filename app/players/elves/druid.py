from abc import ABC
from app.players.elves.elf import Elf


class Druid(Elf, ABC):

    def __init__(self, favourite_spell, nickname, musical_instrument):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self._favourite_spell}"

    def get_rating(self):
        return len(self._favourite_spell)
