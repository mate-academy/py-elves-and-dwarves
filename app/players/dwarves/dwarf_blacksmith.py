from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, skill_level: int, favourite_dish: str):
        super().__init__(favourite_dish)
        self._skill_level = skill_level
        self._nickname = nickname

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self._nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level

    def eat_favourite_dish(self) -> None:
        print(f"{self._nickname} is eating {self._favourite_dish}")