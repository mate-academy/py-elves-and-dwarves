from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """Dwarf player specializing in blacksmithing."""

    def __init__(
        self, nickname: str, favourite_dish: str, skill_level: int
    ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        """Return the skill level."""
        return self._skill_level

    def player_info(self) -> str:
        """Return dwarf blacksmith description with skill level."""
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )
