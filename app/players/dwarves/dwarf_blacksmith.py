from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, favourite_dish: str, skill_level: int) -> None:
        super().__init__(favourite_dish)
        self._skill_level = skill_level
