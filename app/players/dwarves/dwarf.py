from app.players.player import Player
# from dwarf_warrior import DwarfWarrior
# from dwarf_blacksmith import DwarfBlacksmith


class Dwarf(Player):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favorite_dish = favourite_dish

    def get_rating(self):
        if isinstance(self, Dwarf):
            if isinstance(self, DwarfWarrior):
                return self._hummer_level + 4
            else:
                return self._skill_level

    def player_info(self):
        if isinstance(self, Dwarf):
            if isinstance(self, DwarfWarrior):
                return (f"Dwarf warrior {self.nickname}. {self.nickname} has "
                        f"a hummer of the {self._hummer_level} level")
            else:
                return (f"Dwarf blacksmith {self.nickname} with skill of the "
                        f"{self._skill_level} level")

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favorite_dish}")