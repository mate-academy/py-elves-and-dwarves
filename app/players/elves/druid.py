from abc import ABC
from app.players.elves.elf import Elf


class Druid(Elf, ABC):

    def __init__(self, name, favourite_spell):
        super().__init__(name)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.name}. {self.name} has a favourite spell: {self._favourite_spell}"

    def get_rating(self):
        return len(self._favourite_spell)
