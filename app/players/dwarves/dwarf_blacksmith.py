from app.player.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level):
        super().__init__(nickname, skill_level)
        self._skill_level = skill_level
        self._favorite_dish = favorite_dish

    def player_info(self):
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level")

    def get_rating(self):
        return self.skill_level