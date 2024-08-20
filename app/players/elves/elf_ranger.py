from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, musical_instrument: str, bow_level: int) -> None:
        super().__init__(musical_instrument)
        self._bow_level = bow_level
