from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, musical_instrument: str, favourite_spell: str) -> None:
        super().__init__(musical_instrument)
        self._favourite_spell = favourite_spell
