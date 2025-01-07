from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname, favourite_spell: str, musical_instrument: str):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)