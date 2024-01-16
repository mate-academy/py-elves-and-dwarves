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
        dwarf_nick_str = f"Dwarf warrior {self.nickname}."
        dwarf_has_hum_str = f"{self.nickname} has a hummer"
        dwarf_hum_lvl_str = f"of the {self._hummer_level} level"
        return f"{dwarf_nick_str} {dwarf_has_hum_str} {dwarf_hum_lvl_str}"

    def get_rating(self) -> int:
        return self._hummer_level + 4
