from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 hummer_level: int,
                 favourite_dish: str,
                 nickname: str
                 ) -> None:
        self.__hummer_level = hummer_level
        super().__init__(favourite_dish, nickname)

    def get_rating(self) -> int:
        return self.__hummer_level + 4

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self.__hummer_level} level"
