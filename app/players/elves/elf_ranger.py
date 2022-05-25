from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return self._bow_level * 3

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self._bow_level} level"
