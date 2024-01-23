from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return ("Elf ranger {}. {} has bow of the {} level"
                .format(self.nickname, self.nickname, self._bow_level))
