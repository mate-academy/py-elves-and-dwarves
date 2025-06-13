from app.players.elves.elf import Elf

class Druid(Elf):
    def __init__(self, favourite_spell, musical_instrument, nickname):
        super().__init__(musical_instrument, nickname)
        self.favourite_spell = favourite_spell


    def player_info(self):
        return f"""Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"""


    def get_rating(self):
        return len(self.favourite_spell)
