from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int) -> str:
        self._skill_level = skill_level

    def player_info(self, nickname, skill_level):
        return f"Dwarf blacksmith {nickname} with skill of the {skill_level} level"

    def get_rating(self, skill_level):
        return skill_level
