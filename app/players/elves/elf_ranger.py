from __future__ import annotations

from players.elves.elf import Elf


class ElfRanger(Elf):
    """Elf Ranger class."""

    def __init__(self, nickname: str, musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self._bow_level: int = int(bow_level)

    def get_rating(self) -> int:
        """Rating is 3 * bow_level."""
        return 3 * self._bow_level

    def player_info(self) -> str:
        """Return info string for Elf Ranger."""
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )
