from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favorite_dish: str,skill_level: int) -> None:
        super().__init__(nickname, favorite_dish)
        self.skill_level = skill_level

    def player_info(self) -> None:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"

    def get_rating(self) -> str:
        return str(self.skill_level)