from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self._bow_level} level"
