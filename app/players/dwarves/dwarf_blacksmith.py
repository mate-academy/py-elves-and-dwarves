from .dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    
    def __init__(self, skill_level, nickname, favourite_dish):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self):
        return self._skill_level

    def print_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"
