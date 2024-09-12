from app.players.dwarves import dwarf


class DwarfBlacksmith(dwarf.Dwarf):
    def __init__(self, skill_level: int, nickname, favourite_dish):
        self._skill_level = skill_level
        super().__init__(nickname, favourite_dish)

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with " \
               f"skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level
