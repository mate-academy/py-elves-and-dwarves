from app.players.dwarves import dwarf


class DwarfBlacksmith(dwarf.Dwarf):
    def __init__(
            self,
            nickname: str,
            skill_level: int,
            favourite_dish: str
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith "
                f"{self.nickname} with skill of the "
                f"{self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
