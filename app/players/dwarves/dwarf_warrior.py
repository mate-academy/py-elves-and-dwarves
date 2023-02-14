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
        level = self._hummer_level
        return (f"Dwarf warrior {nick}. {nick} has "
                f"a hummer of the {level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4
