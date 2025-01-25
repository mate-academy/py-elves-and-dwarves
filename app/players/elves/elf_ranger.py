from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level : int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        nnam = self.nickname
        bowl = self._bow_level
        return f"Elf ranger {nnam}. {nnam} has bow of the {bowl} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
