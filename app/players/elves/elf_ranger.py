from app.players.elves import Elf

class ElfRanger(Elf):
    def __init__(self, nickname, bow_level):
        super().__init__(nickname)
        self._bow_level = bow_level

    def get_rating(self):
        pass

    def player_info(self):
        pass

