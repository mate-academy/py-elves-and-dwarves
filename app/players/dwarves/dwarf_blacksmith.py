from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super(DwarfBlacksmith, self).__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        first_part = f"Dwarf blacksmith {self.nickname}"
        second_part = f" with skill of the {self._skill_level} level"
        return first_part + second_part
