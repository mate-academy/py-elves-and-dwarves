from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        dwarf_nick_str = f"Dwarf blacksmith {self.nickname}"
        dwarf_skill_str = f"with skill of the {self._skill_level} level"
        return (f"{dwarf_nick_str} {dwarf_skill_str}")

    def get_rating(self) -> int:
        return self._skill_level
