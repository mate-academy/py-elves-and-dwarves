from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, hummer_level: int, favourite_dish: str) -> None:
        super().__init__(favourite_dish)
        self._hummer_level = hummer_level
        self._nickname = nickname

    def player_info(self) -> str:
        return (f"Dwarf warrior {self._nickname}. {self._nickname} "
                f"has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def eat_favourite_dish(self) -> None:
        print(f"{self._nickname} is eating {self._favourite_dish}")
