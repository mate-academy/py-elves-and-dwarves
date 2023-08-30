from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 name: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        first_part = f"Dwarf warrior {self.name}."
        second_part = f" {self.name} has a hummer"
        third_part = f" of the {self.hummer_level} level"
        return first_part + second_part + third_part

    def get_rating(self) -> int:
        return self._hummer_level + 4
