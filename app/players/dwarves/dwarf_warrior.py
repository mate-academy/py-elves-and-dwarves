from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(self, **kwargs) -> None:
        nickname = kwargs.get("nickname")
        favourite_dish = kwargs.get("favourite_dish")
        hummer_level = kwargs.get("hummer_level")
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        result = str(f"Dwarf warrior {self.nickname}. {self.nickname}")
        result += " has a hummer"
        result += str(f" of the {self._hummer_level} level")
        return result

    def get_rating(self) -> int:
        return self._hummer_level + 4
