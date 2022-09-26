from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(self, nickname, musical_instrument, bow_level: int):
        super(ElfRanger, self).__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return F"Elf ranger {self.nickname}. " \
               F"{self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self):
        return self._bow_level * 3
