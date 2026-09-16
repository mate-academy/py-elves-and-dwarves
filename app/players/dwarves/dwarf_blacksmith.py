class DwarfBlacksmit(Dwarf):
    def __init__(self, skill_level: int) -> None:
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill \
            of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
