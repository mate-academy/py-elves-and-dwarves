from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish, skill_level):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level