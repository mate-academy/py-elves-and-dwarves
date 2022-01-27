from app.players.elves.elf import Elf


class ElfRanger(Elf):

    RATING_COEFFICIENT = 3

    def __init__(self, nickname: str, musical_instrument: str, bow_level: int):
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow" \
               f" of the {self._bow_level} level"

    def get_rating(self):
        return self.RATING_COEFFICIENT * self._bow_level
