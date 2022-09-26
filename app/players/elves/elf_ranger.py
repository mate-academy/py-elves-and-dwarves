from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(self, nickname, musical_instrument, bow_level):
        super(ElfRanger, self).__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self.bow_level = bow_level

    def get_rating(self):
        return 3 * self.bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the {self.bow_level} level"
