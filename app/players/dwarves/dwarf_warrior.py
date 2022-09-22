from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def player_info(self) -> str:
        nick = self.nickname
        hummer = self._hummer_level
        part1 = f"Dwarf warrior {nick}. "
        part2 = f"{nick} has a hummer of the {hummer} level"
        return part1 + part2

    def get_rating(self) -> int:
        return self._hummer_level + 4
