from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
        self,
        bow_level: int,
        nickname: str,
        musical_instrument: str,
    ) -> None:

        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        string = (f"Elf ranger {self.nickname}."
                  f" {self.nickname} has bow"
                  f" of the {self._bow_level} level")
        return string

    def get_rating(self) -> int:
        return 3 * self._bow_level
