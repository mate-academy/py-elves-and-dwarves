from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        nick = self.nickname
        hummer_lvl = self._hummer_level
        return f"Dwarf warrior {nick}. " \
               f"{nick} has a hummer of the {hummer_lvl} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4
