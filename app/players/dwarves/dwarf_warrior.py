from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    """Dwarf player specializing in warrior combat."""

    def __init__(
        self, nickname: str, favourite_dish: str, hummer_level: int
    ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        """Return hummer level plus 4."""
        return self._hummer_level + 4

    def player_info(self) -> str:
        """Return dwarf warrior description with hummer level."""
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the "
            f"{self._hummer_level} level"
        )
