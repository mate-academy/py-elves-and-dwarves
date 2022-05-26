from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self._favourite_spell}"

    def get_rating(self):
        return len(self._favourite_spell)
