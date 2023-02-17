from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(favourite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        string = (f"Dwarf warrior {self.nickname}."
                  f" {self.nickname} has a hummer"
                  f" of the {self._hummer_level} level")
        return string

    def get_rating(self) -> int:
        return self._hummer_level + 4
