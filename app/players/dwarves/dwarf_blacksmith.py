from dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, _favourite_dish: str, nickname: str, _skill_level: int) -> None:
        super().__init__(_favourite_dish, nickname)
        self._skill_level = _skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
