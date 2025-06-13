from app.players.dwarves.dwarf import Dwarf


class Dwarf_Warrior(Dwarf):
    def __init__(self, hummer_level, favourite_dish, nickname):
        super().__init__(favourite_dish, nickname)
        self.hummer_level = hummer_level


    def player_info(self):
        return f"""Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level"""


    def get_rating(self):
        return self.hummer_level + 3
