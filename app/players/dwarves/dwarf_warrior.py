from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        self._nickname = nickname
        self._favourite_dish = favourite_dish
        self._hummer_level = hummer_level

    def eat_favourite_dish(self) -> None:
        print(f"{self._nickname} is eating {self._favourite_dish}")

    def player_info(self) -> str:
        return (f"Dwarf warrior {self._nickname}. {self._nickname} "
                f"has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4
