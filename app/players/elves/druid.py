from app.player.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell):
        super().__init__(nickname, favourite_spell)
        self._favourite_spell = favourite_spell
        self._musical_instrument = musical_instrument

    def player_info(self):
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}")

    def get_rating(self):
        return len(self._favourite_spell)