from app.players.dwarves.dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, skill_level):
        super().__init__(nickname)
        self._skill_level = skill_level

    def get_rating(self):
        return self._skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} \
                with skill of the {self.skill_level} level"