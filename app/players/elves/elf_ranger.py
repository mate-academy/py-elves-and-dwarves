from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str = None,
            musical_instrument: str = None,
            bow_level: int = None
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int | float:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the " \
               f"{self._bow_level} level"
