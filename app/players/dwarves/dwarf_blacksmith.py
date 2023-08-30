from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self,
                 name: str,
                 favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        description = f"Dwarf blacksmith {self.name}"
        return description + f" with skill of the {self.skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level
