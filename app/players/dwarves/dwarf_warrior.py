from app.players.dwarf import Dwarves

class DwarfWarrior(Dwarves):
    def __init__(self,
                 name: str,
                 favourite_dish: str,
                 hammer_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._hammer_level = hammer_level

    def player_info(self) -> str:
        return "Dwarf warrior {self.nickname} "\
            "has a hummer of the {self._hammer_level} level"

    def get_rating(self) -> int:
        return len(self._hammer_level + 4)
