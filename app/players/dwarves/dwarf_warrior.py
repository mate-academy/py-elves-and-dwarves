from .dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 hummer_level: int,
                 nickname: str,
                 favourite_dish: str) -> None:
        super().__init__(favourite_dish, nickname)
        self.hummer_level = hummer_level

    def player_info(self) -> None:
        return (f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self.hummer_level} level")

    def get_rating(self) -> None:
        return 4 + self.hummer_level
