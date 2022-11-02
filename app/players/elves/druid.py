from app.players.elves import Elf

class Druid(Elf):
    def __init__(self, nickname, favourite_spell):
        super().__init__(nickname)
        self.favourite_spell = favourite_spell