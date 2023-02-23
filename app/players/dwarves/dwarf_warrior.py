class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int) -> str:
        self._hummer_level = hummer_level

    def player_info(self, nickname, hummer_level):
        return f"Dwarf warrior {nickname}. {nickname} has a hummer of the {hummer_level} level"

    def get_rating(self, hummer_level):
        return hummer_level + 4