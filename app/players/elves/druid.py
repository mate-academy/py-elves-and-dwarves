from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell: str):
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def get_rating(self):
        return len(self.favourite_spell)

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} has " \
               f"a favourite spell: {self.favourite_spell}"
