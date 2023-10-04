from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
        self, favourite_dish: str, nickname: str, skill_level: int
    ) -> None:
        self._skill_level = skill_level
        super().__init__(favourite_dish, nickname)

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the " \
               f"{self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level
