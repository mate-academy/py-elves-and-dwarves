from __future__ import annotations
from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """Elf ranger class with a bow."""

    def __init__(self, nickname: str, musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level: int = bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
                f"{self._bow_level} level")
