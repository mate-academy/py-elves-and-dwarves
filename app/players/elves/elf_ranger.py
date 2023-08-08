from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        nk = self.nickname
        bl = self._bow_level
        return f"Elf ranger {nk}. {nk} has bow of the {bl} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
