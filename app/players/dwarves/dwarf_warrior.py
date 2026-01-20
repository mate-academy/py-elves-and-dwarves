from .dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            hummer_level: int,
            favourite_dish: str | None = None
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the {self.hummer_level} level"
        )

    def get_rating(self) -> int:
        return self.hummer_level + 4
