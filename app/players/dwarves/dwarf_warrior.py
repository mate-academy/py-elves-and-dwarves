from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(favourite_dish)
        self._hummer_level = hummer_level
