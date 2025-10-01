from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level