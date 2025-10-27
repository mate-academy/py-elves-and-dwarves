from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell
