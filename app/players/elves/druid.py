from app.players.elves import Elf

class Druid(Elf):
    def __init__(self, nickname, favourite_spell):
        super().__init__(nickname)
        self._favourite_spell = favourite_spell

    def get_rating(self):
        pass

    def player_info(self):
        pass
