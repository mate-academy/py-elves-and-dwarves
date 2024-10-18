from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        """Get player info."""
        return (f"Druid {self.nickname}. {self.nickname} "
                f"has a favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        """Get player rating."""
        return len(self._favourite_spell)
