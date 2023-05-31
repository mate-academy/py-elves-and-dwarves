from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
        self, nickname: str,
        musical_instrument: str,
        bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level: str = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow "
                f"of the {self.bow_level} level")

    def get_rating(self) -> int:
        return 3 * self.bow_level

    @property
    def bow_level(self) -> int:
        return self._bow_level
