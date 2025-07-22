from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str,
                 favourite_dish: str, hammer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hammer_level = hammer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}."
                f" {self.nickname} has a hammer of the "
                f"{self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4
