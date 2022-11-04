from app.players.dwarves import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, skill_level):
        super().__init__(nickname)
        self._skill_level = skill_level

    def get_rating(self):
        pass

    def player_info(self):
        pass