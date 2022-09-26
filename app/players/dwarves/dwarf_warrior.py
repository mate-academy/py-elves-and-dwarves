from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish, hummer_level):
        super().__init__(nickname, favourite_dish)
        self.__hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}." \
               f" {self.nickname} has a hummer of the" \
               f" {self.__hummer_level} level"

    def get_rating(self):
        return self.__hummer_level + 4
