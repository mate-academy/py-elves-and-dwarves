from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, favourite_dish: str, nickname: str):
        super().__init__(favourite_dish, nickname)
        self.hummer_level = hummer_level

    def player_info(self):
        return (f"Dwarf warrior {self.nickname}. {self.nickname} has "
                f"a hummer of the {self.hummer_level} level")

    def get_rating(self):
        return int(self.hummer_level) + 4
