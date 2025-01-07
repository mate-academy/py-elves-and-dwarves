from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, skill_level: int, favourite_dish: str):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level
