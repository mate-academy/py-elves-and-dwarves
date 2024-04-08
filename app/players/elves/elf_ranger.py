from app.players.elves.elf import Elf


class ElfRanger(Elf):

    _bow_level: int

    def __init__(self,
                 bow_level: int,
                 nickname: str,
                 musical_instrument: str) -> None:

        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level
        self.musical_instrument = musical_instrument

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level

    _bow_level: int
