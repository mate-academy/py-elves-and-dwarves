from app.players.dwarves import dwarf


class DwarfBlacksmith(dwarf.Dwarf):

    def __init__(self, skill_level, favourite_dish, nickname):
        super().__init__(favourite_dish, nickname)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the " \
               f"{self._skill_level} level"

    def get_rating(self):
        return self._skill_level
