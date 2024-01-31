from .dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str,
                 favourite_dish: str, skill_level: int) -> None:
        self._skill_level = skill_level
        super().__init__(nickname, favourite_dish)

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self._skill_level} level")
