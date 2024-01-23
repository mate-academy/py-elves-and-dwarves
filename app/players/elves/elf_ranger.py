from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname,
            musical_instrument,
            bow_level
    ):
        super(ElfRanger, self).__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")

    def get_rating(self):
        return self._bow_level * 3

    def player_info(self):
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the {self._bow_level} level"
