from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):

    def __init__(
            self,
            skill_level: int,
            nickname: str,
            favourite_dish: str
    ) -> None:
        self._skill_level = skill_level
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
