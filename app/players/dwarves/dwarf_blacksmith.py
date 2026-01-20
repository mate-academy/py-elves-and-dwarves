from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, favourite_dish: str, nickname: str):
        super().__init__(favourite_dish, nickname)
        self.skill_level = skill_level

    def player_info(self):
        return (f"Dwarf blacksmith {self.nickname} with skill "
                f"of the {self.skill_level} level")

    def get_rating(self):
        return int(self. skill_level)
