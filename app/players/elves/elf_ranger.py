from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:

        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> float:
        pass

    def player_info(self) -> dict:
        pass
