from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)
        self._bow_level = bow_level
