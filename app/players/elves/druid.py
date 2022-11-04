from app.players.elves import Elf

class Druid(Elf):
    def __init__(self, nickname, favourite_spell):
        super().__init__(nickname)
        self._favourite_spell = favourite_spell

    def get_rating(self):
        return len(self._favourite_spell)

    def player_info(self):
        return f"Druid {self.nickname}. \
               {self.nickname} has a favourite spell: {self.favourite_spell}"
