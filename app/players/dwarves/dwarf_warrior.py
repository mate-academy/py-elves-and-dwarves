from dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 hummer_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self.hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level"

    def get_rating(self) -> int:
        return self.hummer_level + 4
