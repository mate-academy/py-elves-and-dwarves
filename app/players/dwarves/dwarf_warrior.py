from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
            self, nickname: str,
            hummer_level: int,
            favourite_dish: str
    ) -> None:
        super().__init__(nickname)
        self.nickname = nickname
        self._favourite_dish = favourite_dish
        self.__hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname}" \
               f" has a hummer of the {self.__hummer_level} level"

    def get_rating(self) -> int:
        return self.__hummer_level + 4
