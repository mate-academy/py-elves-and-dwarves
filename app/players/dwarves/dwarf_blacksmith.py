from app.players.dwarves import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, skill_level):
        super().__init__(nickname)
        self._skill_level = skill_level
