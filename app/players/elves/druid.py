from app.players.elves import elf


class Druid(elf.Elf):
    def __init__(self, favourite_spell: str, nickname, musical_instrument):
        self._favourite_spell = favourite_spell
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has " \
               f"a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
