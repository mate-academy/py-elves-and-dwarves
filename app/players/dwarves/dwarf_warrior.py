from app.player.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level):
        super().__init__(nickname, hummer_level)
        self._hummer_level = hummer_level
        self._favorite_dish = favorite_dish

    def player_info(self):
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level")

    def get_rating(self):
        return self.hummer_level + 4