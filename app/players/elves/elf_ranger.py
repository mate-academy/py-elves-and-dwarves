from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int | float
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def player_info(self) -> None:
        return f"elves ranger {self.nickname}. {self.nickname}" \
               f" has bow of the {self.bow_level} level"

    def get_rating(self) -> None:
        return 3 * self.bow_level
