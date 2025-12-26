from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish, skill_level):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill " \
               f"of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
