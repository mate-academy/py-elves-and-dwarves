from .elf import Elf

class Druid(Elf):
    def __init__(self, favourite_spell, nickname: str, musical_instrument: str):
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def player_info(self):
        return f"{self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"

    def get_rating(self):
        return len(self.favourite_spell)