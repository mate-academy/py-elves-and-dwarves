from __future__ import annotations

from players.elves.elf import Elf


class Druid(Elf):
    """Druid class (a type of Elf)."""

    def __init__(
        self, nickname: str, musical_instrument: str, favourite_spell: str
    ) -> None:
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self._favourite_spell: str = favourite_spell

    def get_rating(self) -> int:
        """Rating is the length of the favourite spell string."""
        return len(self._favourite_spell)

    def player_info(self) -> str:
        """Return info string for Druid."""
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
        )
