from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 skill_level: int
                 ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self.skill_level = skill_level

    @property
    def skill_level(self) -> int:
        return self._skill_level

    @skill_level.setter
    def skill_level(self, value: int) -> None:
        self._skill_level = value

    def get_rating(self) -> int:
        return self.skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with " \
               f"skill of the {self.skill_level} level"
