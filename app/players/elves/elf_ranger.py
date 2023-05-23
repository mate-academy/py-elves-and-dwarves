from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:

        elf = self.nickname
        bow = self._bow_level

        return (f"Elf ranger {elf}. "
                f"{elf} has bow of the {bow} level")
