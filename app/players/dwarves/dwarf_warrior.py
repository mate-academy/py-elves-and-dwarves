"""
This is specific class for dwarf-warrior.
It inherits all the methods from Player and
Dwarf classes, and adds one additional method
particularly for the dwarf-warrior. All of player`s
instances should be created from this class, if
dwarf-warrior type is choosed to play with.
"""


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

    def get_rating(self):
        return self._hummer_level + 4

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hummer_level} level"
