from players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    # `DwarfWarrior` should be a child of `Dwarf`.
    # Its `__init__` method should take one additional parameter:
    # `hummer_level` - an integer that shows the power of the hummer.
    # The `__init__` method should store it in the protected attribute.
    def __init__(self, nickname: str,
                 favourite_dish: str, hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        # `get_rating` method should return:
        # * `hummer_level` + 4 for `DwarfWarrior`
        return 4 + self._hummer_level

    def player_info(self) -> str:
        # * `"Dwarf warrior {nickname}. {nickname} has a
        # hummer of the {hummer_level} level"` for `DwarfWarrior` instances
        return (f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self._hummer_level} level")
