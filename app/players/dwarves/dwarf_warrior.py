from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int = 0) -> None:
        self._hammer_level = hummer_level
        super().__init__(nickname, favourite_dish)

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. "\
            f"{self.nickname} has a hummer of the {self._hammer_level} level"

    def get_rating(self) -> int:
        return self._hammer_level + 4
