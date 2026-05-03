from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str,
                 favourite_dish: str, skill_level: int) -> None:
        self._skill_level = skill_level
        super().__init__(nickname, favourite_dish)

    def player_info(self) -> str:
        name = self.nickname
        skill = self._skill_level
        return f"Dwarf blacksmith {name} with skill of the {skill} level"

    def get_rating(self) -> int:
        return self._skill_level
