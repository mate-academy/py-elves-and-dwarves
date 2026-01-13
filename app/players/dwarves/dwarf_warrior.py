from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        nick = self.nickname
        hummer = self._hummer_level
        first_str = f"Dwarf warrior {nick}. "
        second_str = f"{nick} has a hummer of the {hummer} level"
        return first_str + second_str

    def get_rating(self) -> int:
        return self._hummer_level + 4
