from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, favourite_dish, nickname):
        super().__init__(favourite_dish, nickname)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} " \
               f"with skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
