from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 bow_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        calculate_rating = 3 * self._bow_level
        return calculate_rating

    def player_info(self) -> str:
        info = (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self._bow_level} level")
        return info
