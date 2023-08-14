from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self, nickname:
            str, bow_level: int,
            musical_instrument: str
    ) -> None:
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
