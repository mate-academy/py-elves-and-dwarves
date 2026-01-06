from app.players.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level):
        super().__init__(nickname, bow_level)
        self._bow_level = bow_level
        self._musical_instrument = musical_instrument

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {bow_level} level")

    def get_rating(self):
        return 3 * self._bow_level