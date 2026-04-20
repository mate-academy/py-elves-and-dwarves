from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """Elf player specializing in ranged bow combat."""

    def __init__(
        self, nickname: str, musical_instrument: str, bow_level: int
    ) -> None:
        super().__init__(
            nickname=nickname, musical_instrument=musical_instrument
        )
        self._bow_level = bow_level

    def get_rating(self) -> int:
        """Return 3 times the bow level."""
        return self._bow_level * 3

    def player_info(self) -> str:
        """Return elf ranger description with bow level."""
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )
