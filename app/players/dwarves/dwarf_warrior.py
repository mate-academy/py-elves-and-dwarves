from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int | float
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def player_info(self) -> None:
        return f"dwarves warrior {self.nickname}. {self.nickname}" \
               f" has a hummer of the {self.hummer_level} level"

    def get_rating(self) -> None:
        return self.hummer_level + 4
