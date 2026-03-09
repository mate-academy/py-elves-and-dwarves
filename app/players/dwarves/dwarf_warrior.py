from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """Concrete class representing a Dwarf warrior."""
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        """
        Initialize a DwarfWarrior object with
        nickname, favourite dish and hummer level.
        """
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        """
        Calculate and return the dwarf warrior's rating based on hummer level.
        """
        return self._hummer_level + 4

    def player_info(self) -> str:
        """
        Return a string with the dwarf warrior's detailed information.
        """
        return (f"Dwarf warrior {self.nickname}. {self.nickname}"
                f" has a hummer of the {self._hummer_level} level")
