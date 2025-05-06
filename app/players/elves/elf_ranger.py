from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
        self, nickname: str, _musical_instrument: str, _bow_level: int
    ) -> None:
        super().__init__(nickname, _bow_level)
        self._bow_level = _bow_level

    def get_rating(self) -> int:
        return (3 * self._bow_level)

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}."
            f"{self.nickname} has bow of the {self._bow_level} level"
        )
