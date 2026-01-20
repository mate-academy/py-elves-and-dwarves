from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(self, musical_instrument, nickname, bow_level: int):
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the {self._bow_level} level"
