from app.players.elves import Elf

class ElfDruid(Elf):
    def __init__(self,
                 name: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(name, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return "Druid {self.nickname} "\
            "has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)