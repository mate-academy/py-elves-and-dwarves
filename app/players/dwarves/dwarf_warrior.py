class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, favorite_dish: str, nickname: str) -> None:
        super().__init__(favorite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4