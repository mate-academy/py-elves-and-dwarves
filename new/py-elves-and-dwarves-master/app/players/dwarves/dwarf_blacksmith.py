from app.players.dwarves.dwarf import Dwarf


class Dwarf_Blacksmith(Dwarf):
    def __init__(self, skill_level, favourite_dish, nickname):
        super().__init__(favourite_dish, nickname)
        self.skill_level = skill_level

    def player_info(self):
        return f"""Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"""


    def get_rating(self):
        return self. skill_level