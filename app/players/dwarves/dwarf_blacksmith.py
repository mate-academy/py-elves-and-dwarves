from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):

    def __init__(self, nickname, favourite_dish, skill_level):
        super(DwarfBlacksmith, self).__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self.skill_level = skill_level

    def get_rating(self):
        return self.skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with " \
               f"skill of the {self.skill_level} level"
