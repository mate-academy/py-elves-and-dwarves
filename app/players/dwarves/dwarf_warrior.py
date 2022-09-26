from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf,):

    def __init__(self, nickname, favourite_dish, hummer_level):
        super(DwarfWarrior, self).__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self.hummer_level = hummer_level

    def get_rating(self):
        return 4 + self.hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. " \
               f"{self.nickname} has a hummer of " \
               f"the {self.hummer_level} level"
