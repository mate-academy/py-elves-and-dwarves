from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def get_rating(self):
        return self.hummer_level + 4

    def player_info(self):
        return (
            f"Dwarf warrior {self.nickname}. ",
            f"{self.nickname} has a hummer of the {self.hummer_level} level"
        )
