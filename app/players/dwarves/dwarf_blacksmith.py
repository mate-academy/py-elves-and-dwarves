from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._skill_level = skill_level

    def player_info(self) -> str:
        """Get player info."""
        return (f"Dwarf blacksmith {self.nickname} with "
                f"skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        """Get player rating."""
        return self._skill_level
