from app.players.elves.elf import Elf

class ElfRanger(Elf):
    def __init__(self, bow_level):
        self._bow_level = bow_level

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self):
        return 3 * self._bow_level