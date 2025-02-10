from app.players.dwarves.dwarf import Dwarf
class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int):
        self._hummer_level = hummer_level

    def player_info(self):
        return (f"Dwarf warrior {self.nickname}. "
                f"{self.nickname} has a hummer of the {self.hummer_level} level")

    def get_rating(self):
        return self._hummer_level + 4
