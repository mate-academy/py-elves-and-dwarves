from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self.skill_level = skill_level

    def get_rating(self) -> int:
        return self.skill_level

    def print_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level")
