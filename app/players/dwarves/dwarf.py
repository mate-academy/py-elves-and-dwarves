from app.players.player import Player


class Dwarf(Player):
    """Intermediate class for Dwarf race."""
    def __init__(
            self,
            nickname: str,
            favourite_dish: str
    ) -> None:
        """Initialize a Dwarf with nickname and a favourite dish."""
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """Print a message about the dwarf eating their favourite dish."""
        print(f"{self.nickname} is eating {self._favourite_dish}")
