from app.players.elves import Elf

class ElfRanger(Elf):
    def __init__(self, nickname, bow_level):
        super().__init__(nickname)
        self._bow_level = bow_level

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. \
               {self.nickname} has bow of the {self.bow_level} level"

