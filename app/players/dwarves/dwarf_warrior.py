from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):

    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:

        dwarf = self.nickname
        skill = self._hummer_level

        return (f"Dwarf warrior {dwarf}."
                f" {dwarf} has a hummer of the {skill} level")
