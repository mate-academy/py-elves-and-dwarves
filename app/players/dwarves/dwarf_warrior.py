from app.players.dwarves import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname, hummer_level):
        super().__init__(nickname)
        self._hummer_level = hummer_level

    def get_rating(self):
        pass

    def player_info(self):
        pass

