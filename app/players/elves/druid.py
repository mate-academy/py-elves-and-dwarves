from app.players.elves.elf import Elf


class Druid(Elf):
    """Elf player specializing in magic and spells."""

    def __init__(
        self, nickname: str, musical_instrument: str, favourite_spell: str
    ) -> None:
        super().__init__(
            nickname=nickname, musical_instrument=musical_instrument
        )
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        """Return the length of the favourite spell."""
        return len(self._favourite_spell)

    def player_info(self) -> str:
        """Return druid description with favourite spell."""
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: "
            f"{self._favourite_spell}"
        )
