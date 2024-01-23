from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
