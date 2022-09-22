from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell, musical_instrument, nickname):
        super().__init__(musical_instrument, nickname)
        self._favourite_spell = favourite_spell

    def player_info(self):
        print(f"Druid {self.nickname}. "
              f"{self.nickname} has a favourite spell: "
              f"{self._favourite_spell}")

    def get_rating(self):
        return len(self._favourite_spell)
