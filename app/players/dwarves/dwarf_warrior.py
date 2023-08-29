from dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, name: str, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.name}. {self.name} has a hummer of the {self.hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4
