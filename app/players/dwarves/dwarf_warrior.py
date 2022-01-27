from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int):
        super().__init__(nickname, favourite_dish)
        self._hammer_level = hummer_level

    def get_rating(self):
        return self._hammer_level + 4

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hammer_level} level"
