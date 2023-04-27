from app.players.player import Player
from app.players.elves.elf import Elf
class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell: str):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell