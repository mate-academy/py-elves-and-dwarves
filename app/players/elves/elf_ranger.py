from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return "Elf ranger {0}. {0} has bow of the {1} level".format(
            self.nickname,
            self._bow_level
        )

    def get_rating(self):
        return 3 * self._bow_level
