from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return "Dwarf warrior {0}. {0} has a hummer of the {1} level".format(
            self.nickname,
            self._hummer_level
        )

    def get_rating(self):
        return self._hummer_level + 4
