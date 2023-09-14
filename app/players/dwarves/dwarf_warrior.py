from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int
                 ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self.hummer_level = hummer_level

    @property
    def hummer_level(self) -> int:
        return self._hummer_level

    @hummer_level.setter
    def hummer_level(self, value: int) -> None:
        self._hummer_level = value

    def get_rating(self) -> int:
        return self.hummer_level + 4

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has " \
               f"a hummer of the {self.hummer_level} level"
