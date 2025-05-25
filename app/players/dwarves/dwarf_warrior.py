from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
        self.__hummer_level = hummer_level
        super().__init__(nickname, favourite_dish)

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.__hummer_level} level"

    def get_rating(self) -> int:
        return self.__hummer_level + 4
