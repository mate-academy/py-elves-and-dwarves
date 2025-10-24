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

    def get_rating(self) -> int:
        return self._hummer_level * 9

    def player_info(self) -> str:
        return (
            f"Dwarf Warrior {self.nickname} eats {self._favourite_dish} "
            f"and fights with hummer level {self._hummer_level}"
        )
