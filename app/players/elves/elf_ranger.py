from app.players.elves import elf


class ElfRanger(elf.Elf):

    def __init__(self, bow_level, musical_instrument, nickname):
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has" \
               f" bow of the {self._bow_level} level"

    def get_rating(self):
        return self._bow_level * 3
