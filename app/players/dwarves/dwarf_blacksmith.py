from .dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self,
                 skill_level: int,
                 nickname: str,
                 favourite_dish: str) -> None:
        super().__init__(favourite_dish, nickname)
        self.skill_level = skill_level

    def player_info(self) -> None:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self.skill_level} level")

    def get_rating(self) -> None:
        return self.skill_level
