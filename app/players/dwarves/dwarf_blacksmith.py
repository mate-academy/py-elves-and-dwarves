from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.protected = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the {self.protected} level"

    def get_rating(self):
        return self.protected
