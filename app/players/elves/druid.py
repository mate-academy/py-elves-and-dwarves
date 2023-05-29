from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str, musical_instrument, nickname):
        super().__init__(musical_instrument, nickname)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self._favourite_spell}"

    def get_rating(self):
        return len(self._favourite_spell)
