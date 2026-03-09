from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    """Concrete class representing a Dwarf blacksmith."""
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        """
        Initialize a DwarfBlacksmith object with
        nickname, favourite dish and skill level.
        """
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        """
        Calculate and return the dwarf blacksmith's rating
        based on their skill level.
        """
        return self._skill_level

    def player_info(self) -> str:

        return (f"Dwarf blacksmith {self.nickname}"
                f" with skill of the {self._skill_level} level")
