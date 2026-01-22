from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} "
              f"has bow of the {self._bow_level} level")
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self._bow_level} level"

    def get_rating(self):
        print("ElfRanger", 3 * self._bow_level)
        return float(3 * self._bow_level)
