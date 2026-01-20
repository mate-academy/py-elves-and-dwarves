from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        """Get player info."""
        return (f"Dwarf warrior {self.nickname}. {self.nickname} "
                f"has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        """Get player rating."""
        return self._hummer_level + 4
